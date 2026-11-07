---
title: Notebooks Jupyter
description: Exécutez des Notebooks Jupyter dans PlaidCloud pour l'analyse interactive de données, la visualisation et l'exploration de données en Python.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/jupyter-notebook.md
---

Jupyter Notebook et Jupyter Lab offrent des capacités interactives remarquables pour analyser, explorer, expliquer et présenter des données.  PlaidCloud permet d'utiliser vos informations directement dans les notebooks.

PlaidCloud fournit JupyterHub dans chaque espace de travail tenant, s'il est activé.  La documentation ci-dessous vous aide à configurer Jupyter séparément, sur un poste de travail ou sur un serveur distinct.

## Installer Jupyter Notebook
Cette section suppose que vous disposez d'une installation de Jupyter Notebook fonctionnelle.

### Installer un Jupyter Notebook autonome
Pour en savoir plus sur l'installation locale d'un Jupyter Notebook, consultez [la documentation d'installation de Jupyter](https://jupyter.org/install).

### Ajouter à VS Code
VS Code propose également une extension qui permet d'exécuter des notebooks directement dans VS Code.  Installez l'extension depuis le [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)


## Installer les utilitaires PlaidCloud
Bien que PlaidCloud soit accessible au moyen de requêtes OAuth et API REST standard, nous vous recommandons d'utiliser nos bibliothèques prêtes à l'emploi pour simplifier l'accès. En outre, la bibliothèque PlaidCloud Utilities inclut des outils pratiques pour manipuler les données avec les dataframes Pandas.

Pour installer les utilitaires PlaidCloud, exécutez les installations pip suivantes :

```bash
pip install "plaidcloud-rpc>=1.25.0" plaidcloud-utilities
```

La version 1.25.0 de `plaidcloud-rpc` est la première à envoyer ses appels à l'API REST. Les versions antérieures utilisent JSON-RPC, qui est obsolète et sera supprimé dans une publication ultérieure.

## Obtenir un jeton OAuth

Consultez [Configuration d'OAuth](/fr/reference/cli/jupyter/oauth-setup/) pour savoir comment obtenir un jeton OAuth et configurer le système pour l'authentification automatisée.


## Ouvrir l'interface utilisateur de Jupyter Notebook

Lancez votre serveur de notebooks pour commencer.



Une fois connecté à votre serveur de notebooks Jupyter, créez un nouveau notebook depuis l'interface.

Un notebook vierge s'ouvre.



Créez une connexion pour communiquer avec PlaidCloud via les points de terminaison de l'API

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection()
```


Établissez un objet table local, puis interrogez-le ; les résultats sont placés automatiquement dans un dataframe [Pandas](https://pandas.pydata.org/).

```python
tbl_sf_cust_master = conn.get_table('Salesforce_Customer_Master') # This gets a table object
df_sf_cust_master = conn.get_data(tbl_sf_cust_master) # This retrieves all the data into a dataframe
```


Avec ce même objet table, vous pouvez aussi écrire des requêtes plus avancées en syntaxe SQLAlchemy standard.

```python
df_sf_cust_master_w_sales = conn.get_data(
    tbl_sf_cust_master.select().with_only_columns(
        [tbl_sf_cust_master.c.Id, tbl_sf_cust_master.c.CurrencyIsoCode, tbl_sf_cust_master.c.SyDSalesRegion]
    ).where(
        tbl_sf_cust_master.c.TotalSalesPast3Years > 0
    )
)
```
