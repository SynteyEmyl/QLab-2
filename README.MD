# hydro-wave-visualizer

This project consists of five elements:
- src
- Numerical Simulation of the Probability Distribution in a Wave Function.pdf
- NSPDHAWF - Presentation.pdf
- Python Installation Manual With Libraries.pdf
- QLab App - Use Manual.pdf

The paper (Numerical Simulation of the Probability
Distribution in a Wave Function.pdf) and implementation
describes the use of Monte Carlo's Integration method to
numerically simulate the behavior of the probability
distribution in the real valued Wave Functions of the
Hydrogen atom. The paper also mentions and develops the
general integration of the probability distribution in a
general wave function.

The document 'NSPDHAWF - Presentation.pdf' is a beamer like
presentation which as all the .pdf files in this repository
was written in LaTeX.

This project is licensed under MIT License, comply with the
Digital Millennium Copyright Act: 17 U.S.C. §§ 101, 104,
104A, 108, 132, 114, 117, 701

**Remember** to include the MIT Licence and the original
creator of this project (all them if derived subsequent times).

## Instructions

### Installing the Dependencies
#### Linux (bash)
    $ cd hydro-wave-visualizer/
    $ python3 -m venv env
    $ source env/bin/activate
    $ pip install matplotlib pandas openpyxl

#### Windows (CMD)
    > cd hydro-wave-visualizer/
    > python -m venv venv
    > env/bin/activate.bat
    > pip install matplotlib pandas openpyxl

### Using the program
#### Linux (bash)
    $ cd hydro-wave-visualizer/
    $ source env/bin/activate
    $ python3 hydro_wave_visualizer.py

#### Windows (CMD)
    > cd hydro-wave-visualizer/
    > env/bin/activate.bat
    > python hydro_wave_visualizer.py

To execute the code in a clearer way, I'm suggesting you 
to create a new virtual environment and adding the 
dependencies the project needs via pip ONLY in the virtual
environment. This is because you won't want to install
every package you need globally but for the project you're
working with.

That and the fact that packages are cached so that if you
need them again, these will be loaded from local.

## Monte Carlo Integral of H1s
<p align="center">
    <img src="doc/monte-carlo-squared_h1s.png" width="350" height="350" style="margin: 0 1rem"/>
</p>

## Monte Carlo Integral of H2s
<p align="center">
    <img src="doc/monte-carlo-squared_h2s.png" width="350" height="350" style="margin: 0 1rem"/>
</p>

## Monte Carlo Integral of H2p
<p align="center">
    <img src="doc/monte-carlo-squared_h2p.png" width="350" height="350" style="margin: 0 1rem"/>
</p>

## Monte Carlo Integral of H3s
<p align="center">
    <img src="doc/monte-carlo-squared_h3s.png" width="350" height="350" style="margin: 0 1rem"/>
</p>

## Monte Carlo Integral of H3p
<p align="center">
    <img src="doc/monte-carlo-squared_h3p.png" width="350" height="350" style="margin: 0 1rem"/>
</p>

## Monte Carlo Integral of H3d
<p align="center">
    <img src="doc/monte-carlo-squared_h3d.png" width="350" height="350" style="margin: 0 1rem"/>
</p>
