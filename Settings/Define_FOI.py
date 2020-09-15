# -*- coding: utf-8 -*-
"""
DEFINE FUEL/OXIDIZER/INERT

Created on Tue Jun 30 16:28:00 2020

@author: Alberto Cuadra Lara
         PhD Candidate - Group Fluid Mechanics
         Office 1.1.D17, Universidad Carlos III de Madrid
"""
import numpy as np
from Solver.Functions.SetSpecies import SetSpecies
from Solver.Functions.ComputeProperties import ComputeProperties
from NASA_database.set_element_matrix import set_element_matrix

def add_species(self, Species):
    for species in Species:
            if species not in self.S.List_Compute_Species:
                # Add species and index in the compute and index list, respectively
                self.S.List_Compute_Species.append(species) 
                self.S.ind_all.append(self.S.N_Compute_Species)
                # Add one row to A0 and M0 matrix, respectively
                self.C.A0.Value = np.concatenate((self.C.A0.Value, np.zeros((1, self.E.NE))))
                self.C.M0.Value = np.concatenate((self.C.M0.Value, np.zeros((1, 12))))
                self.C.N0.Value = self.C.M0.Value[:, [0, 9]] 
                # Obtain the formula of the species
                txFormula = self.strThProp[species].txFormula 
                # Obtain the element matrix
                self.strThProp[species].Element_matrix = set_element_matrix(
                    txFormula, self.E.ElementsUpper) 
                # Obtain index of the elements that compound the species and the number of atoms of each element
                ind_Elements, atoms = (self.strThProp[species].Element_matrix[0, :], self.strThProp[species].Element_matrix[1, :])
                # Update A0 matrix
                for ind_Element, atom in zip(ind_Elements, atoms):
                    self.C.A0.Value[self.S.N_Compute_Species, int(ind_Element)] = atom
                # Increase one the number of species 
                self.S.N_Compute_Species += 1
    return (self.S.List_Compute_Species, self.C.M0.Value)


def Define_F(self, Species=None):
    if Species:  # not empty, i.e., there is/are fuel/s in the mixture
        self.PD.S_Fuel, self.PD.N_Fuel = unpack_dict(Species)
        self.S.List_Compute_Species, self.C.M0.Value = add_species(self, self.PD.S_Fuel)
        self.PD.R_Fuel = SetSpecies(
            self, self.PD.S_Fuel, self.PD.N_Fuel, self.PD.TR.Value)
        self.PS.strR_Fuel = ComputeProperties(
            self, self.PD.R_Fuel, self.PD.pR.Value, self.PD.TR.Value)
        self.PD.Fuel.x = self.PS.strR_Fuel.NatomE[self.E.ind_C]
        self.PD.Fuel.y = self.PS.strR_Fuel.NatomE[self.E.ind_H]
        self.PD.Fuel.z = self.PS.strR_Fuel.NatomE[self.E.ind_O]
        self.PD.Fuel.w = self.PS.strR_Fuel.NatomE[self.E.ind_N]
        self.PD.phi.t = self.PD.Fuel.x + self.PD.Fuel.y / 4 - self.PD.Fuel.z / 2
    return self


def Define_O(self, Species=None):
    self.PD.S_Oxidizer, self.PD.N_Oxidizer = unpack_dict(Species)
    self.S.List_Compute_Species, self.C.M0.Value = add_species(self, self.PD.S_Oxidizer)
    if Species:  # not empty, i.e., there is/are oxidizer/s in the mixture
        self.PD.R_Oxidizer = SetSpecies(
            self, self.PD.S_Oxidizer, self.PD.N_Oxidizer, self.PD.TR.Value)
    return self


def Define_I(self, Species=None):
    if Species:  # not empty, i.e., there is/are oxidizer/s in the mixture
        self.PD.S_Inert, self.PD.N_Inert = unpack_dict(Species)
        self.S.List_Compute_Species, self.C.M0.Value = add_species(self, self.PD.S_Inert)
        self.PD.R_Inert = SetSpecies(
            self, self.PD.S_Inert, self.PD.N_Inert, self.PD.TR.Value)
    else:
        self.PD.R_Inert = 0
    if self.PD.S_Oxidizer or self.PD.S_Inert:
        self.PS.strR_Oxidizer_and_Inert.append(ComputeProperties(
            self, self.PD.R_Oxidizer + self.PD.R_Inert, self.PD.pR.Value, self.PD.TR.Value))
    return self


def Define_FOI(self, i):
    R = self.PD.R_Fuel + self.PD.R_Oxidizer + self.PD.R_Inert
    self.PS.strR.append(ComputeProperties(self, R, self.PD.pR.Value,
                                          self.PD.TR.Value))
    self.PS.strR[i].phi = self.PD.phi.Value[i]
    return self


def unpack_dict(dictionary):
    return (tuple(dictionary), list(dictionary.values()))
