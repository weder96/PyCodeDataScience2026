import numpy as np
import pandas as pd
from scipy import stats

def main():    
    rs = np.random.RandomState(24)
    n = 20
    t = 10    

    x = np.linspace(0, t, 100)
    s = np.array([stats.gamma.pdf(x, a) for a in [3, 5, 7]])
    d = s[:, np.newaxis, :]

    d = d * np.array([1, -1])[rs.binomial(1, .3, 3)][:, np.newaxis, np.newaxis]
    d = d + rs.normal(0, .15, (3, n))[:, :, np.newaxis]
    d = d + rs.uniform(0, .25, 3)[:, np.newaxis, np.newaxis]
    d *= 10
    
    # Transpõe o array para a ordem (subject, timepoint, ROI)
    # A dimensão de 'd' agora é (20, 100, 3)
    d = d.transpose((1, 2, 0))

    # 1. Defina os rótulos para cada dimensão
    subjects = np.arange(n)
    timepoints = x
    rois = ["IPS", "AG", "V1"]

    # 2. Crie um MultiIndex com todas as combinações de rótulos
    index = pd.MultiIndex.from_product(
        [subjects, timepoints, rois], 
        names=["subject", "timepoint", "ROI"]
    )

    # 3. Crie o DataFrame "tidy" diretamente
    #    - d.flatten() transforma o array 3D em um vetor 1D na ordem correta.
    #    - O Series usa o MultiIndex para rotular cada ponto de dado.
    #    - reset_index() converte os níveis do índice em colunas.
    df = pd.Series(d.flatten(), index=index, name="BOLD signal").reset_index()
    
    # Salva o DataFrame em um arquivo CSV
    path ="../result/"
    df.to_csv(path+"gammas.csv", index=False)

    print("Arquivo 'gammas.csv' criado com sucesso!")
    print("Primeiras 5 linhas do DataFrame:")
    print(df.head())


if __name__ == "__main__":
    main()