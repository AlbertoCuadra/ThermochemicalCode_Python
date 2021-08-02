# Combustion PyToolbox
A Python based thermochemical code

Table of contents
=================

<!--ts-->
   * [Introduction](#Introduction)
   * [Getting Started](#Getting-Started)
   * [Prerequisites](#Prerequisites)
   * [Installing](#Installing)
   * [Running the tests](#Running-the-tests)
   * [Built With](#Built-With)
   * [Contributing](#Contributing)
   * [Versioning](#Versioning)
   * [Authors](#Authors)
   * [License](#License)
   * [Acknowledgments](#Acknowledgments)
   
<!--te-->

## Introduction
As a first step towards the development of a wider-scope thermochemical tool, in this work we present a thermochemical code with application to gaseous combustion problems recently implemented by the authors in MATLAB and `Python`. The python version solves, by the moment, one chemical equilibrium problems (TP transformations; where T denotes temperature, P pressure), assuming always ideal gases. The `Python` version has not all the capabilities as the MATLAB version has, because it is much slower than this. When I or we (community) fix this bottleneck I will continue with the development of this version adding all the capabilities the MATLAB version has. I will also add a GUI using Qt5 and Pyside2. \newline

The code computes the equilibrium composition by minimization of the Gibbs–Helmholtz free energy, and employs NASA’s 9-coefficient polynomial fits to evaluate the thermodynamic properties. Results computed with **Combustion-Toolbox** have been validated against, and are in good agreement with, NASA’s Chemical Equilibrium with Applications (CEA) program and CANTERA.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

MATLAB or Python

```
Give examples
```

### Installing



## Running the tests


## Built With


## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning


## Authors

* **[Alberto Cuadra-Lara](https://github.com/AlbertoCuadra)<sup>1</sup>** - *Programmer and App designer*
* **Marcos Vera<sup>1</sup>** - *Programmer*  
<sup>1</sup>  Grupo de Mecánica de Fluidos, Universidad Carlos III, Av. Universidad 30, 28911, Leganés, Spain

See also the list of [contributors](https://github.com/AlbertoCuadra/combustion_toolbox/blob/master/CONTRIBUTORS.md) who participated in this project.

## License


## Acknowledgments
