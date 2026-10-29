---
title: Jupyter-Notebooks
description: Führen Sie Jupyter-Notebooks in PlaidCloud für interaktive Datenanalyse, Visualisierung und Python-basierte Datenexploration aus.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/jupyter-notebook.md
---

Jupyter-Notebooks und JupyterLab bieten hervorragende interaktive Möglichkeiten, Daten zu analysieren, zu untersuchen, zu erläutern und darüber zu berichten.  PlaidCloud ermöglicht die Nutzung von Informationen direkt in Notebooks.

PlaidCloud stellt in jedem Mandanten-Workspace JupyterHub bereit, sofern es aktiviert ist.  Die folgende Dokumentation hilft Ihnen bei der Einrichtung von Jupyter auf einem Desktop oder einem separaten Server.

## Jupyter-Notebook installieren
Dabei wird vorausgesetzt, dass Sie über eine funktionierende Jupyter-Notebook-Installation verfügen.

### Eigenständiges Jupyter-Notebook installieren
Weitere Informationen zur lokalen Installation eines Jupyter-Notebooks finden Sie in der [Installationsdokumentation von Jupyter](https://jupyter.org/install).

### Zu VS Code hinzufügen
VS Code bietet außerdem eine Erweiterung, mit der Sie Notebooks direkt in VS Code ausführen können.  Installieren Sie die Erweiterung über den [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)


## PlaidCloud Utilities installieren
Auf PlaidCloud kann zwar über Standard-OAuth und JSON-RPC-Anfragen zugegriffen werden, wir empfehlen jedoch die Verwendung unserer vorgefertigten Bibliotheken für einen einfacheren Zugriff.  Außerdem enthält die Bibliothek PlaidCloud Utilities praktische Datenhilfen für die Arbeit mit Pandas-DataFrames.

Um PlaidCloud Utilities zu installieren, führen Sie die folgenden pip-Installationen aus:

```bash
pip install plaidcloud-rpc@git+https://github.com/PlaidCloud/plaid-rpc.git@v1.4.0#egg=plaidcloud-rpc
```

```bash
pip install plaidcloud-utilities@git+https://github.com/PlaidCloud/plaid-utilities.git@v1.5.2#egg=plaidcloud-utilities
```

## OAuth-Token abrufen

Weitere Informationen zum Abrufen eines OAuth-Tokens und zur Konfiguration des Systems für die automatisierte Authentifizierung finden Sie unter [OAuth-Einrichtung](/de/reference/cli/jupyter/oauth-setup/).


## Benutzeroberfläche des Jupyter-Notebooks öffnen

Starten Sie Ihren Notebook-Server, um zu beginnen.



Sobald Sie bei Ihrem Jupyter-Notebook-Server angemeldet sind, erstellen Sie in der Benutzeroberfläche ein neues Notebook.

Dadurch wird ein leeres Notebook geöffnet.



Erstellen Sie eine Verbindung, um über die API-Endpunkte mit PlaidCloud zu kommunizieren

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection()
```


Erstellen Sie ein lokales Tabellenobjekt und fragen Sie es dann ab. Die Ergebnisse werden automatisch in einem [Pandas](https://pandas.pydata.org/)-DataFrame abgelegt.

```python
tbl_sf_cust_master = conn.get_table('Salesforce_Customer_Master') # This gets a table object
df_sf_cust_master = conn.get_data(tbl_sf_cust_master) # This retrieves all the data into a dataframe
```


Mit demselben Tabellenobjekt können Sie auch komplexere Abfragen in der Standard-SQLAlchemy-Syntax schreiben.

```python
df_sf_cust_master_w_sales = conn.get_data(
    tbl_sf_cust_master.select().with_only_columns(
        [tbl_sf_cust_master.c.Id, tbl_sf_cust_master.c.CurrencyIsoCode, tbl_sf_cust_master.c.SyDSalesRegion]
    ).where(
        tbl_sf_cust_master.c.TotalSalesPast3Years > 0
    )
)
```
