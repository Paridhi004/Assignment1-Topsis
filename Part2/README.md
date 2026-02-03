# TOPSIS Python Package

**Topsis-Paridhi-102303715** is a Python package for solving **Multiple Criteria Decision Making (MCDM)** problems using the Technique for Order Preference by Similarity to Ideal Solution (TOPSIS)**.

This package allows users to rank alternatives based on multiple criteria by providing:
- a CSV input file
- a weight vector
- an impact vector

The package computes the **TOPSIS score** and **rank** for each alternative.

---

## Installation

Use the package manager `pip` to install the package:

```bash
pip install Topsis-Paridhi-102303715
```

## Usage: 

```bash
topsis <input_file.csv> "<weights>" "<impacts>" <output_file.csv>
```
Example
topsis sample.csv "0.25,0.25,0.25,0.25" "+,+,-,+" output.csv


## Input File Format:
Enter the CSV filename followed by the .csv extension

## PyPI link
https://pypi.org/project/Topsis-Paridhi-102303715/

