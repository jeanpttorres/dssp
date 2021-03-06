## Introduction
This repository stores general information about the **dataset** we have artificially generated for the Distinguishing String Selection Problem (DSSP) and the Distinguishing Substring Selection Problem (DSSSP). 

We are publishing here the **input files** for the instances, the **solutions** we have found, a **solution checker**, and **tables** comparing the performance of the algorithms.

 
## Problems

 - Distinguishing String Selection Problem (DSSP)
 - Distinguishing Substrin Selection Problem (DSSSP)

## Algorithms

 - **exact**: a 30 minutes execution of the branch-and-bound algorithm applying the mathematical model described in [1];
 - **ra**: the **rounding algorithm** proposed in [2];
 - **bcpa**: an adaptation from the **basic core problem algorithm** also proposed in [2];
 - **ilpbn-vns**: a VNS implementation which applies the Mathematical Model in order to define its Neighbourhood Structure;
 - **ilpbs-vns**: a VNS based matheuristic which expands the ilpbn by applying the Mathematical Model in the Shaking and Local Search steps.

## Dataset
Let ***n*** be the size of the set ***Sc*** of Strings and ***m*** be the length of every string in  ***Sc***, the following datasets are available:

 - g1: *m* >> *n*
 - g2: *m* > *n*
 - g3: *n* > *m*

## Solutions
The target string we found applying every algorithm in each string from those sets above are reported in the **solutions** folder.

## Tables
The values and results we found applying every algorithm in each string from those sets above are reported in the **results** folder.

## Validator

The folder validator contains a Python file called checker.py that can be used to validate solutions for the DSSP and DSSSP. 

Usage:
python check.py [instance-file-name] [solution-file-name]

## External Reference

[1] Meneses, C.N., Pardalos, P.M., Resende, M.G.C., Vazacopoulos, A.: Modeling and solvingstring selection problems.  In: Proceedings of the Second International Symposium on Mathematical and Computational Biology, pp. 54–64 (2005)

[2] Della Croce, F., Salassa, F.: Improved lp-based algorithms for theclosest string problem. Computers & Operations Research

