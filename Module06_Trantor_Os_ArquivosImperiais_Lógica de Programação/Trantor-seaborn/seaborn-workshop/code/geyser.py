import numpy as np
import pandas as pd
from scipy.cluster.vq import kmeans2

if __name__ == "__main__":

    np.random.seed(0)
    
    # Instead of loading everything and renaming, we specify which columns to use.
    # This ignores extra columns (like an unwanted index column) 
    # and prevents the "Length mismatch" error.
    try:
        df = pd.read_csv("../../data/raw/geyser.csv", usecols=["duration", "waiting"])
    except FileNotFoundError:
        print("Error: 'geyser.csv' file not found.")
        print("Please make sure the file is in the correct directory.")
        exit() # Exits the script if the file doesn't exist

    # K-means is run to find 3 clusters
    # 'centroids' stores the coordinates of the cluster centers
    # 'labels' stores the cluster ID (0, 1, or 2) for each data point
    centroids, labels = kmeans2(df[["duration", "waiting"]], 3)

    # Maps the numeric labels (0, 1, 2) to text labels
    cluster_map = {0: "short", 1: "long", 2: "medium"}
    df["kind"] = pd.Series(labels).map(cluster_map)

    # Saves the final result to a new file
    path ="../result/"
    df.to_csv(path+"geyser_clustered.csv", index=False)
    
    print("'geyser_clustered.csv' file created successfully!")
    print("\nFirst few lines of the resulting DataFrame:")
    print(df.head())
    
    print("\nCount of eruptions by type:")
    print(df["kind"].value_counts())