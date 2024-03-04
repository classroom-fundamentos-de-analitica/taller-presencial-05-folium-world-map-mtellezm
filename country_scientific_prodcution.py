"""Taller Presencial Evaluable"""


import pandas as pd

def load_affiliations():
    dataframe = pd.read_csv(
        "https://raw.githubusercontent.com/jdvelasq/datalabs/master/datasets/scopus-papers.csv",
        sep=",", 
        index_col=None,
    )[["Affiliations"]]
    return dataframe
    


def remove_na_rows(affiliations):
    """Elimina las filas con valores nulos en la columna 'Affiliations'"""

    affiliations = affiliations.copy()
    affiliations = affiliations.dropna(subset=["Affiliations"])

    return affiliations
  

df = load_affiliations()
df = remove_na_rows(df)
print(df.sort_values("Affiliations").head())
print(df.sort_values("Affiliations".tail()))