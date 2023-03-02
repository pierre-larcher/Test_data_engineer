""""Description.

Librairie de la troisième partie.
"""

import pandas as pd
import json
import numpy


# EXERCICE 1

with open("products.json") as mon_fichier:
    product_list = json.load(mon_fichier)


def clean_cat(produit: str) -> str:
    """Supprime les champs NULL de chaque catégorie d'un dictionnaire produit.

    Exemple:
    >>> clean_cat({'idappcat': '2076,3B,19C,138D,NULL,NULL',
    ...  'refproduitenseigne': 364980,
    ...  'libelle': 'Nature bio champignons émincés 230g ',
    ...  'categorieenseigne': ''})
    {'idappcat': '2076,3B,19C,138D', 'refproduitenseigne': 364980, 'libelle': 'Nature bio champignons émincés 230g ', 'categorieenseigne': ''}
    """
    for key, value in produit.items():
        try:
            produit[key] = value.replace(",NULL", "")
        except:
            pass
    return produit


def clean_cat_all_product(produits: list[dict]) -> list[dict]:
    """Applique la fonction clean_cat à tous les dictionnaires produits."""
    for produit in produits:
        produit = clean_cat(produit)
    return produits


# EXERCICE 2


def import_raw_data():
    """Importe les bases de données des magasins et des référentiels d'actifs."""
    df1 = pd.read_csv("17-10-2018.3880.gz", sep=";")
    df1["Date"] = pd.to_datetime("17-10-2018")
    df2 = pd.read_csv("18-10-2018.3880.gz", sep=";")
    df2["Date"] = pd.to_datetime("18-10-2018")
    df_shop = pd.concat([df1, df2])
    df_shop.reset_index(drop=True, inplace=True)
    df_asset = pd.read_csv("back_office.csv.gz", sep=",")
    df_asset = df_asset.rename(columns={"pe_ref_in_enseigne": "identifiantproduit"})
    return df_shop, df_asset


def process_data(df_shop: pd.DataFrame, df_asset: pd.DataFrame) -> pd.DataFrame:
    """Merge la base de données des magasins avec celle des référentiels d'actifs."""
    df_shop["identifiantproduit"] = df_shop["identifiantproduit"].astype("str")
    df_asset["identifiantproduit"] = df_asset["identifiantproduit"].astype("str")
    df_shop = df_shop.merge(df_asset, on=["identifiantproduit"])
    return df_shop


# data = process_data(import_raw_data()[0], import_raw_data()[1])

# EXERCICE 3


def average_prices(data: pd.DataFrame):
    """Créer un fichier csv avec l'identifiant des produits dans une colonne et la moyenne des prix dans une autre."""
    data = data.groupby(["identifiantproduit"]).mean().round(2).reset_index()
    colonnes = ["identifiantproduit", "prixproduit"]
    data = data[colonnes]
    data = data.rename(columns={"prixproduit": "prixmoyen"})
    return data.to_csv(
        "average_prices.csv", index=False, header=True, sep=";", encoding="utf-8-sig"
    )


# EXERCICE 4


def count_products_by_categories_by_day(data: pd.DataFrame) -> pd.DataFrame:
    """Compte le nombre de produits différents par catégories Dataimpact, détaillants et dates."""
    colonnes = ["Date", "categorieenseigne", "p_id_cat", "identifiantproduit"]
    data = data[colonnes]
    data = (
        data.groupby(["Date", "categorieenseigne", "p_id_cat"])
        .size()
        .reset_index(name="nombreproduit")
        .drop_duplicates(subset="p_id_cat")
    )
    data.reset_index(drop=True, inplace=True)
    return data


def average_products_by_categories(data: pd.DataFrame) -> pd.DataFrame:
    """Fait la moyenne du nombre de produits des deux jours par Dataimpact et détaillants."""
    data = count_products_by_categories_by_day(data)
    colonnes = ["categorieenseigne", "p_id_cat", "nombreproduit"]
    data = data[colonnes]
    data.groupby(["categorieenseigne", "p_id_cat"]).apply(
        lambda x: numpy.average(x["nombreproduit"])
    ).reset_index()
    data = data.rename(columns={"nombreproduit": "nombremoyenproduit"})
    return data
