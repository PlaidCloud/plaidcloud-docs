---
title: Notebooki Jupyter
description: Uruchamiaj Notebooki Jupyter w PlaidCloud do interaktywnej analizy danych, wizualizacji i eksploracji danych w Pythonie.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/jupyter-notebook.md
---

Notebooki Jupyter i Jupyter Lab zapewniają znakomite interaktywne możliwości analizowania, eksplorowania, objaśniania i raportowania danych.  PlaidCloud umożliwia korzystanie z informacji bezpośrednio w notebookach.

PlaidCloud udostępnia JupyterHub w każdym obszarze roboczym dzierżawy, jeśli został on aktywowany.  Poniższa dokumentacja pomaga skonfigurować Jupyter osobno na komputerze stacjonarnym lub oddzielnym serwerze.

## Instalacja Jupyter Notebook
Zakłada się, że masz działającą instalację Jupyter Notebook.

### Instalacja samodzielnego Jupyter Notebook
Więcej informacji o lokalnej instalacji Jupyter Notebook znajdziesz w [dokumentacji instalacji Jupyter](https://jupyter.org/install).

### Dodawanie do VS Code
VS Code udostępnia również rozszerzenie, które pozwala uruchamiać notebooki bezpośrednio w VS Code.  Zainstaluj rozszerzenie z [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)


## Instalacja narzędzi PlaidCloud Utilities
Chociaż dostęp do PlaidCloud jest możliwy za pomocą standardowych żądań OAuth i JSON-RPC, zalecamy korzystanie z naszych gotowych bibliotek, które upraszczają dostęp.  Ponadto biblioteka PlaidCloud Utilities zawiera przydatne funkcje pomocnicze do pracy z ramkami danych Pandas.

Aby zainstalować PlaidCloud Utilities, wykonaj następujące instalacje pip:

```bash
pip install plaidcloud-rpc@git+https://github.com/PlaidCloud/plaid-rpc.git@v1.4.0#egg=plaidcloud-rpc
```

```bash
pip install plaidcloud-utilities@git+https://github.com/PlaidCloud/plaid-utilities.git@v1.5.2#egg=plaidcloud-utilities
```

## Uzyskiwanie tokenu OAuth

Więcej informacji o uzyskiwaniu tokenu OAuth i konfigurowaniu systemu do zautomatyzowanego uwierzytelniania znajdziesz w sekcji [Konfiguracja OAuth](/pl/reference/cli/jupyter/oauth-setup/).


## Otwieranie interfejsu użytkownika Jupyter Notebook

Uruchom serwer notebooków, aby rozpocząć.



Po zalogowaniu do serwera notebooków Jupyter utwórz nowy notebook z poziomu interfejsu.

Otworzy się pusty notebook.



Utwórz połączenie do komunikacji z PlaidCloud przez punkty końcowe API

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection()
```


Utwórz lokalny obiekt tabeli, a następnie zapytaj go, aby wyniki trafiły automatycznie do ramki danych [Pandas](https://pandas.pydata.org/).

```python
tbl_sf_cust_master = conn.get_table('Salesforce_Customer_Master') # This gets a table object
df_sf_cust_master = conn.get_data(tbl_sf_cust_master) # This retrieves all the data into a dataframe
```


Za pomocą tego samego obiektu tabeli możesz też pisać bardziej zaawansowane zapytania w standardowej składni SQLAlchemy.

```python
df_sf_cust_master_w_sales = conn.get_data(
    tbl_sf_cust_master.select().with_only_columns(
        [tbl_sf_cust_master.c.Id, tbl_sf_cust_master.c.CurrencyIsoCode, tbl_sf_cust_master.c.SyDSalesRegion]
    ).where(
        tbl_sf_cust_master.c.TotalSalesPast3Years > 0
    )
)
```
