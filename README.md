# Assignment1-Topsis
# TOPSIS - Python Project

> **Assignment:** Multi-Criteria Decision Making (MCDM) using TOPSIS  
> **Submitted By:** [Paridhi Rastogi]  
> **Roll Number:** [102303715]

## Overview
This project implements the **TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)** algorithm. It is a multi-criteria decision analysis method that compares a set of alternatives based on a specified criterion, weighting, and impact parameters.

The project is divided into three parts:
1.  **Command Line Interface (CLI):** A python script to run TOPSIS locally.
2.  **PyPI Package:** A publicly available Python library for TOPSIS.
3.  **Web Service:** A web application with email integration.

---

## Part 1: Command Line Interface (CLI)

The CLI tool allows users to perform TOPSIS analysis on a CSV file via the terminal.

### Usage
```bash
python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
```
Example:
```bash
python topsis.py data.csv "1,1,1,2,1" "+,+,-,+,-" result.csv
```
### Input Constraints:
Input File Must be a CSV file with 3 or more columns.
1. First Column: Object/Alternative names (text).
2. Other Columns: Numeric parameters only.

### Weights/Impacts: 
Must be separated by commas (,).

### Validation: 
The program automatically checks for file existence, numeric values, and matching dimensions.

## Part 2: PyPI Package
The TOPSIS logic has been packaged and published on PyPI for easy installation.
Package Name: Topsis-Paridhi-102303715
### PyPI Link: 
https://pypi.org/project/Topsis-Paridhi-102303715/

### Syntax: topsis(input_filename, weights, impacts, output_filename)
topsis("data.csv", "1,1,1,1", "+,-,+,+", "output.csv")

## Part 3: Web Service
A user-friendly web interface is deployed to handle TOPSIS calculations without writing code. The results are emailed directly to the user.
### Live Demo: 
[Link to your Render/Vercel App]
### Features:
1. Upload CSV: Drag-and-drop interface.
2. Custom Inputs: Easy input for Weights and Impacts.
3. Email Integration: Results are sent as an attachment to your inbox.
4. Sample Data: Downloadable sample CSV for testing.
