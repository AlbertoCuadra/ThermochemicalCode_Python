# -*- coding: utf-8 -*-
"""
Specify the minority products to be considered in the product mixture (P) in
addition to the major species (CO2, CO, H2O, H2, O2, N2, C(gr)).
Moreover, He and Ar are always included in the database.

Created on Mon Jun 22 12:15:00 2020

@author: Alberto Cuadra Lara
         PhD Candidate - Group Fluid Mechanics
         Office 1.1.D22, Universidad Carlos III de Madrid
"""

def ListSpecies(self, LS='HC/02/N2 EXTENDED'):
    if type(LS) == list:
        self.S.LS = LS
    elif LS.upper() == 'HC/02/N2 EXTENDED':
        self.S.LS = ['CO2', 'CO', 'H2O', 'H2', 'O2', 'N2', 'He', 'Ar',
                     'OH', 'H', 'O', 'HO2', 'NO', 'HCO', 'CH4', 'CH3',
                     'NO2', 'NH3', 'NH2', 'N', 'HCN', 'CN', 'N2O', 'C2', 'CH']
    elif LS.upper() == 'HC/02/N2 RICH':
        self.S.LS = ['CO2', 'CO', 'H2O', 'H2', 'O2', 'N2', 'He', 'Ar',
                     'N2', 'H2O', 'CO', 'HCN', 'H2O', 'CO2', 'H', 'OH',
                     'O', 'CN', 'NH3', 'CH4', 'C2H4', 'CH3', 'NO', 'HCO',
                     'NH2', 'NH', 'N', 'CH']
    elif LS.upper() == 'SOOT FORMATION':
        self.S.LS = ['CO2', 'CO', 'H2O', 'H2', 'O2', 'N2', 'He', 'Ar',
                     'N2', 'H2O', 'CO', 'HCN', 'H2O', 'CO2', 'H', 'OH',
                     'O', 'CN', 'NH3', 'CH4', 'C2H4', 'CH3', 'NO', 'HCO',
                     'NH2', 'NH', 'N', 'CH', 'Cbgrb']
    elif LS.upper() == 'SOOT FORMATION EXTENDED':
        self.S.LS = ['CO2', 'CO', 'H2O', 'H2', 'O2', 'N2', 'He', 'Ar',
                     'H', 'O', 'OH', 'HO2', 'H2O2', 'CH', 'CH2', 'CH3',
                     'CH4', 'HCO', 'CH2OH', 'CH3O', 'CH3OH', 'C2H', 'C2H4',
                     'C2H5', 'C2H6', 'HCCO', 'N', 'NH', 'NH2', 'NH3',
                     'NO', 'NO2', 'N2O', 'HNO', 'CN', 'HCN', 'NCO', 'C3H8',
                     'C2', 'C2H2_acetylene', 'C6H6', 'C8H18_isooctane', 'C2H5OH',
                     'HNC', 'HNCO', 'NH2OH', 'COOH', 'CH2CO_ketene', 'OCCN',
                     'C2N2', 'C2O', 'HCHO_formaldehy', 'C3H4_allene', 'HCOOH',
                     'CH3CHO_ethanal', 'CH3CN', 'C3H6_propylene', 'Cbgrb']
    elif LS.upper() == 'NASA ALL':
        self.S.LS = ['CH3', 'CH4', 'CN', 'CO2', 'C2H', 'CH2CO_ketene',
                                  'C2H3_vinyl', 'C2H4', 'CH3COOH', 'C2H6', 'CH3OCH3', 'CNC', 'C2O',
                                  'C3H3_2_propynl', 'C3H6O_propanal',
                                  'C3H8', 'CNCOCN', 'C4H2_butadiyne', 'C4H6_1butyne', 'C4H8_1_butene',
                                  'C4H8_isobutene', 'C4H9_n_butyl', 'C4H9_t_butyl', 'C4N2',
                                  'C5H11_pentyl', 'C5H12_i_pentane', 'C6H5_phenyl', 'C6H5OH_phenol',
                                  'C7H7_benzyl', 'C7H14_1_heptene', 'C7H16_2_methylh',
                                  'C8H16_1_octene', 'C8H18_isooctane', 'C10H21_n_decyl', 'H', 'HCCN', 'HNCO',
                                  'HNO3', 'HCHO_formaldehy', 'H2O2', 'NCO', 'NH3', 'NO2', 'N2O', 'NH2NO2', 'N2O4',
                                  'N3H', 'O2', 'C2H5OHbLb', 'C6H6bLb', 'H2ObLb', 'CH', 'CH2OH', 'CH3OH',
                                  'CNN', 'COOH', 'C2H2_acetylene', 'ObCHb2O', 'CH3CN', 'C2H4O_ethylen_o',
                                  'OHCH2COOH', 'CH3N2CH3', 'CH3O2CH3', 'OCCN', 'C3', 'C3H4_allene', 'C3H5_allyl',
                                  'C3H6O_propylox', 'C3H7_n_propyl', 'C3H8O_1propanol', 'C3O2',
                                  'C4H6_2butyne', 'C4H8_cis2_buten',
                                  'C4H9_i_butyl', 'C4H10_n_butane', 'C5', 'C5H10_1_pentene', 'C5H11_t_pentyl',
                                  'CH3CbCH3b2CH3', 'C6H5O_phenoxy', 'C6H13_n_hexyl', 'C7H8',
                                  'C7H15_n_heptyl', 'C8H8_styrene', 'C8H17_n_octyl', 'C9H19_n_nonyl', 'C12H9_o_bipheny',
                                  'HCN', 'HCCO', 'HNO', 'HO2', 'HCOOH', 'NH', 'NH2OH', 'NO3', 'NCN', 'N2H4',
                                  'N2O5', 'O', 'O3', 'N2H4bLb', 'CH2',
                                  'CH3O', 'CH3OOH', 'CO', 'C2', 'C2H2_vinylidene', 'HObCOb2OH', 'CH3CO_acetyl',
                                  'CH3CHO_ethanal', 'C2H5', 'C2H5OH', 'CCN', 'C2N2', 'C3H3_1_propynl', 'C3H4_propyne',
                                  'C3H6_propylene', 'C3H6O_acetone', 'C3H7_i_propyl', 'C3H8O_2propanol',
                                  'C4', 'C4H6_butadiene', 'C4H8_tr2_butene',
                                  'C4H9_s_butyl', 'C4H10_isobutane',
                                  'C5H12_n_pentane', 'C6H2', 'C6H6', 'C6H12_1_hexene', 'C6H14_n_hexane',
                                  'C7H8O_cresol_mx', 'C7H16_n_heptane', 'C8H10_ethylbenz', 'C8H18_n_octane',
                                  'C10H8_naphthale', 'C12H10_biphenyl', 'HCO', 'HNC', 'HNO2', 'H2', 'H2O',
                                  'N', 'NH2', 'NO', 'N2', 'N2H2', 'N2O3', 'N3', 'OH', 'CH3OHbLb', 'C6H5NH2bLb', 'He', 'Ar', 'C']
    elif LS.upper() == 'AIR':
        self.S.LS = ['O2', 'N2', 'O', 'O3', 'N', 'NO', 'NO2', 'NO3', 'N2O3', 'N2O4', 'N3', 'C', 'CO', 'CO2',
                     'Ar', 'CH4', 'CH3', 'CH', 'H2O', 'H2', 'H', 'He']
    elif LS.upper() == 'IDEAL_AIR':
        self.S.LS = ['O2', 'N2', 'O', 'O3', 'N', 'NO', 'NO2', 'NO3', 'N2O', 'N2O3', 'N2O4', 'N3']
    elif LS.upper() == 'HYDROGEN':
        self.S.LS = ['H', 'HNO', 'HNO3', 'H2O', 'NH', 'NH2OH', 'NO3', 'N2H2', 'N2O3', 'N3', 'OH', 'HNO2',
                     'H2', 'N', 'NH3', 'NO2', 'N2O', 'N2H4', 'N2O5', 'O', 'O3', 'He', 'Ar', 'CO2', 'CO',
                     'O2', 'N2', 'HO2', 'NH2', 'H2O2', 'N3H', 'NH2NO2']
    else:
        self.S.LS = LS

    self.S.NS = len(self.S.LS)
    
    return self
