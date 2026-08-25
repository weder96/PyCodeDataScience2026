import pandas as pd

def main():

    df = pd.read_csv("../../data/raw/attention.csv")
    df = pd.melt(df, ["subidr", "attnr"], var_name="solutions", value_name="score")
    df.solutions = df.solutions.str[-1].astype(int)
    df.columns = ["subject", "attention", "solutions", "score"]
    path ="../result/"
    df.to_csv(path+"attention.csv")


if __name__ == "__main__":
    main()
