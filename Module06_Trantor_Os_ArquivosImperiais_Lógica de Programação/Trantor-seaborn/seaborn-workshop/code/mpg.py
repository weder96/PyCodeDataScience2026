import pandas as pd


if __name__ == "__main__":
    path ="../result/"
    raw_data = "../../data/raw/mpg.csv"
    df = pd.read_csv(raw_data, na_values="?")
    origin_map = {1: "usa", 2: "europe", 3: "japan"}
    df["origin"] = df["origin"].map(origin_map)
    df.to_csv(path+"mpg.csv", index=False)
