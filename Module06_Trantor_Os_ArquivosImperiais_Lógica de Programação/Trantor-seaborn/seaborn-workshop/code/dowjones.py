import pandas as pd

if __name__ == "__main__":
    path ="../result/"
    (        
        pd.read_csv("../../data/raw/dowjones.csv")
        .set_axis(["Date", "Price"], axis=1)
        .to_csv(path+"dowjones.csv", index=False)
    )
