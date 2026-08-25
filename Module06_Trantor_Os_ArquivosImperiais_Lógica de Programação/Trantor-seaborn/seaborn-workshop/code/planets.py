import pandas as pd

def main():

    raw_data = "../../data/raw/planets.csv"
    df = pd.read_csv(raw_data , skiprows=1)

    print(df.columns)  # print name columns
    print(df.head())   # see first lines to DataFrame

    df.columns = ["method", "number", "orbital_period",
                  "mass", "distance", "year"]
    
    path ="../result/"
    df.to_csv(path+"planets.csv", index=False)


if __name__ == "__main__":
    main()
