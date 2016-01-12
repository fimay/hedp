#   HEDP module

[![Build Status](https://travis-ci.org/luli/hedp.svg?branch=master)](https://travis-ci.org/luli/hedp)

A Python module to analyse High Energy Density (HED) experiments and radiation hydrodynamics simulations.


## Installation

    python setup.py develop --user


## Dependencies
   This module requires Python 2.7, 3.3 or 3.4  with  `numpy`, `scipy`,  `cython`, `pytables` and `opacplot2` ( https://github.com/rth/opacplot2).


 Optional dependencies include:
 - `matplotlib`
 - `beautifulsoup4`
 - The GNU Scientific Library (GSL), required for calculating the Planck/Rosseland means
 - PyEOSPAC (https://github.com/luli/pyeospac), for interfacing with the tabulated EoS
 - `nose`, for running the test suite

## List of features
  
####   File formats `hedp.io`

   - parser for the Andor `.sif` image files
   - parser for the Hamamatsu streak camera `.img` files

#### Equation of state (EoS) and opacities
   - Kramer-Unsoldt opacity model
   - generation of a database with cold henke opacities
   - Thomas Fermi pressure ionization.
   - Calculation of Planck and Rosseland (gray/mutigroup) means
   - Automatic group selection for multigroup opacities
   - General interpolators intended for visualisation for the EoS and opacity tables (requires [opacplot](https://github.com/rth/opacplot2) and [pyeospac](https://github.com/luli/pyeospac) modules).


####  Basic mathematical operators `hedp.math`
   - Gradient for a non-informally sampled 1D or 2D data
   - Savitzky-Golay filter 
   - Integrators for the super-gaussian functions
   - Direct and inverse Abel transforms. The integration is carried out numerically with a semi-analytical handling of the singularity.


#### Plasma physics `hedp.plasma_physics`
   This section defines a few useful quantities required in plasma physics:  the critical density, Coulomb logarithm, electron-ion collision rates, inverse Bremsstrahlung coefficient,  isentropic sound speed, Spitzer conductivity.


#### Visualization  `hedp.viz`
   - Metric formatter for `matplotlib`
         
#### Diagnostics  `hedp.diag`
   - intensity calibration for the self-emission GOI and SOP
   - IP sensitivity curves for x-rays
   

#### Post-processing  `hedp.pp`
   - Calculation of synthetic radiographs from 2D axis-symmetrical hydrodynamic simulation with the Abel transform 
