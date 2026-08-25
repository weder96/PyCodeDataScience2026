import pandas as pd

if __name__ == "__main__":
    path ="../result/"
    (
        pd.read_csv("../../data/raw/glue.csv")        
        .drop(["Task", "Score"], axis=1)
        .melt(id_vars=["Model", "Year", "Encoder"], var_name="Task", value_name="Score")
        .to_csv(path+"glue.csv", index=False)
    )

    print("Arquivo 'glue.csv' transformado e salvo com sucesso!")