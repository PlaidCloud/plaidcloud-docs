---
title: Jupyter Notebooks
slug: jupyter-notebook
weight: 1.0
description: Interact with PlaidCloud directory from Jupyter Notebooks
date: 2022-01-25T07:39:47
---


Jupyter Notebooks and Jupyter Lab provide exceptional interactive capabilities to analyze, explore, explain, and report data.  PlaidCloud enables use of information directly in notebooks.

PlaidCloud provides JupyterHub within each tenant workspace if is activated for use.  The documentation below helps with setting up Jupyter separately on a desktop or seperate server.

## Install Jupyter Notebook
This assumes you have a working Jupyter Notebook installation.

### Installing a Stand-Alone Jupyter Notebook
For more information on installing a Jupyter Notebook locally you can reference [Jupyter’s installation documentation](https://jupyter.org/install).

### Add to VS Code
VS Code also provides an extension that allows you to run notebooks directly in VS Code.  Install the extension from the [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)


## Install PlaidCloud Utilities
While PlaidCloud can be accessed using stand OAuth and JSON-RPC requests, it is recommended that you use our pre-built libraries for simplified access.  In addition, the PlaidCloud utilities library includes handy data helpers for use with Pandas dataframes.

To install the PlaidCloud Utilities perform the following pip installs:

```bash
pip install plaidcloud-rpc@git+https://github.com/PlaidCloud/plaid-rpc.git@v1.4.0#egg=plaidcloud-rpc
```

```bash
pip install plaidcloud-utilities@git+https://github.com/PlaidCloud/plaid-utilities.git@v1.5.2#egg=plaidcloud-utilities
```

## Obtaining an OAuth Token

See [OAuth Tokens](/docs/cli/get-oauth-tokens/) for more information on obtaining an OAuth token and how to configure the system for automated auth.


## Open Jupyter Notebook User Interface

Launch your notebook server to get started.



Once you are signed into your Jupyter notebook server, create a new notebook from the UI.

This will open a blank notebook.



Create a connection to communicate with PlaidCloud through the API endpoints

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection()
```


Establish a local table object and then query it with the results automatically placed in a [Pandas](https://pandas.pydata.org/) dataframe.

```python
tbl_sf_cust_master = conn.get_table('Salesforce_Customer_Master') # This gets a table object
df_sf_cust_master = conn.get_data(tbl_sf_cust_master) # This retrieves all the data into a dataframe
```


With that same table object you can also write more advanced queries using standard SQLAlchemy syntax.

```python
df_sf_cust_master_w_sales = conn.get_data(
    tbl_sf_cust_master.select().with_only_columns(
        [tbl_sf_cust_master.c.Id, tbl_sf_cust_master.c.CurrencyIsoCode, tbl_sf_cust_master.c.SyDSalesRegion]
    ).where(
        tbl_sf_cust_master.c.TotalSalesPast3Years > 0
    )
)
```



