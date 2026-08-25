import pandas as pd


if __name__ == "__main__":

    G7_countries = {
        "USA": "USA",
        "CAN": "Canada",
        "FRA": "France",
        "DEU": "Germany",
        "ITL": "Italy",
        "GBR": "Great Britain",
        "JPN": "Japan",
        # "CHE": "Switzerland",
        # "DNK": "Denmark",
        # "KOR": "Korea",
        # "BRA": "Brazil",
        # "COL": "Colombia",
        # "CHN": "China",
        # "IND": "India",
    }
    path ="../result/"
    (
        pd.read_csv("../../data/raw/healthexp.csv")
        .assign(Country=lambda x: x["Country"].map(G7_countries))
        .dropna(subset=["Country"])
        .query("Year <= 2020")
        .to_csv(path+"healthexp.csv", index=False)
    )
