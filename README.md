# test-driven-dev (TDD)

[![Build Status](https://travis-ci.com/cu-swe4s-fall-2019/test-driven-development-tlfobe.svg?branch=master)](https://travis-ci.com/cu-swe4s-fall-2019/test-driven-development-tlfobe)

# Test Driven Development

This repository is a program for visualizing various datasets.

# Usage

TDD can be used directly with another program that outputs a space separated table. In this repository there are some generate random data files one can use to ensure the program is working as intended.

To generate a histogram of random date use the folling command :
```
bash gen_data.sh | python viz.py --out_file hist.png --plot_type histogram
```

# Installation

