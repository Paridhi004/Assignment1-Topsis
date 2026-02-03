import pandas as pd
import numpy as np
import os

def topsis(input_file, weights, impacts, output_file):

    if not os.path.exists(input_file):
        raise Exception("Input file not found")

    df = pd.read_csv(input_file)

    if df.shape[1] < 3:
        raise Exception("File must have at least 3 columns")

    data = df.iloc[:, 1:].astype(float)

    weights = list(map(float, weights.split(",")))
    impacts = impacts.split(",")

    if len(weights) != data.shape[1] or len(impacts) != data.shape[1]:
        raise Exception("Weights, impacts, and criteria count mismatch")

    for i in impacts:
        if i not in ["+", "-"]:
            raise Exception("Impacts must be + or -")

    norm = np.sqrt((data ** 2).sum())
    normalized = data / norm
    weighted = normalized * weights

    ideal_best, ideal_worst = [], []

    for i in range(len(impacts)):
        if impacts[i] == "+":
            ideal_best.append(weighted.iloc[:, i].max())
            ideal_worst.append(weighted.iloc[:, i].min())
        else:
            ideal_best.append(weighted.iloc[:, i].min())
            ideal_worst.append(weighted.iloc[:, i].max())

    dist_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    dist_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    score = dist_worst / (dist_best + dist_worst)

    df["Topsis Score"] = score
    df["Rank"] = df["Topsis Score"].rank(ascending=False).astype(int)

    df.to_csv(output_file, index=False)
