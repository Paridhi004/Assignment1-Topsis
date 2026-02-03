import sys
import pandas as pd
import numpy as np
import os

def error(msg):
    print(f"Error: {msg}")
    sys.exit(1)

def topsis(input_file, weights, impacts, output_file):
    # ---------- File check ----------
    if not os.path.exists(input_file):
        error("Input file not found")

    # ---------- Read CSV ----------
    try:
        df = pd.read_csv(input_file)
    except Exception:
        error("Unable to read CSV file")

    if df.shape[1] < 3:
        error("Input file must contain at least 3 columns")

    data = df.iloc[:, 1:]

    # ---------- Numeric check ----------
    if not np.issubdtype(data.dtypes.values[0], np.number):
        error("Columns from 2nd to last must be numeric")

    try:
        data = data.astype(float)
    except ValueError:
        error("Non-numeric value found in criteria columns")

    # ---------- Parse weights & impacts ----------
    weights = weights.split(",")
    impacts = impacts.split(",")

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        error("Number of weights, impacts, and criteria must be same")

    try:
        weights = np.array(weights, dtype=float)
    except ValueError:
        error("Weights must be numeric")

    for i in impacts:
        if i not in ["+", "-"]:
            error("Impacts must be either + or -")

    # ---------- Normalization ----------
    norm = np.sqrt((data ** 2).sum())
    normalized = data / norm

    # ---------- Weighted normalization ----------
    weighted = normalized * weights

    # ---------- Ideal best & worst ----------
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    # ---------- Distance calculation ----------
    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # ---------- Topsis score ----------
    score = (dist_worst / (dist_best + dist_worst))*100

    # ---------- Rank ----------
    df["Topsis Score"] = score
    df["Rank"] = df["Topsis Score"].rank(ascending=False, method="dense").astype(int)

    # ---------- Output ----------
    df.to_csv(output_file, index=False)
    print("TOPSIS analysis completed successfully")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        error("Usage: python topsis.py <InputDataFile> <Weights> <Impacts> <OutputFile>")

    _, input_file, weights, impacts, output_file = sys.argv
    topsis(input_file, weights, impacts, output_file)
