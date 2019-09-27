# test-driven-dev (TDD)

[![Build Status](https://travis-ci.com/cu-swe4s-fall-2019/test-driven-development-tlfobe.svg?branch=master)](https://travis-ci.com/cu-swe4s-fall-2019/test-driven-development-tlfobe)

# Test Driven Development

This repository is a program for visualizing various datasets.

# Usage

TDD can be used directly with another program that outputs a space separated table. In this repository there are some generate random data files one can use to ensure the program is working as intended.

To generate a histogram of the first column of random dataset use the following command :
```
bash gen_data.sh | python viz.py --out_file hist.png --plot_type histogram
```

There is also the option to generate a random set of columns of random value and display a select column of this data set:
```
bash gen_data_random.sh | python viz.py --out_file combo.png --plot_type combo
```
If a general program outputs space sparated values, our program can be used with it using the following :
```
call_your_program.exe | python viz.py --out_file boxplot.png --plot_type boxplot
```

# Installation

To install this program, you'll need to make sure your version of Python has all the dependencies required for this program.
The dependencies of this program are shown below : 
- numpy
- matplotlib

These can be install using the following Linux/Unix command line prompt :
```
conda install --yes numpy
conda install --yes matplotlib
```