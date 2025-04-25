# Shopofy: Schottky Position Finder

Command line application that takes the output power from a position-sensitive Schottky detector and returns the position in millimetres.

## Requirements
python version > 3.6 (should work)

## Installation
- Clone or download the repository from github.
- Move to `shopofy/` where `setup.py` is located and run `pip install .`.

## Usage
Once installed, run `shopofy` and simply enter the power value. It will return the position value in mm. By default it uses the R/Q map from the elliptical cavity at RIKEN's R3 ring, simulated by D. Dmytriiev[^1].

If you would like to use your own R/Q map, it must be a two column .csv file with the x position in the first column and the associated impedance in the second column. You can specify the file using `shopofy --rqmap my_rqmap.csv` or simply `shopofy -rq my_rqmap.csv`. An example is included in the `examples` folder.

The command line interface will prompt you for a power, but you can include it in the opening argument, e.g. `shopofy --power 45` or `shopofy -p 45`.

[^1]: D. Dmytriiev, ‘Design of a position sensitive resonant Schottky detector for the Rare-RI Ring in RIKEN’, Dissertation, University of Heidelberg, 2022. doi: 10.11588/heidok.00031183.
