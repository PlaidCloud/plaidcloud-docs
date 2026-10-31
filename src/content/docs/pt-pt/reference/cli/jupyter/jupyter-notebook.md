---
title: Blocos de notas Jupyter
description: Execute blocos de notas Jupyter no PlaidCloud para análise interativa de dados, visualização e fluxos de exploração de dados baseados em Python.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/jupyter-notebook.md
---

Os blocos de notas Jupyter e o Jupyter Lab oferecem capacidades interativas excecionais para analisar, explorar, explicar e reportar dados.  O PlaidCloud permite utilizar a informação diretamente nos blocos de notas.

O PlaidCloud disponibiliza o JupyterHub em cada área de trabalho do inquilino, se estiver ativado para utilização.  A documentação abaixo ajuda a configurar o Jupyter separadamente, num computador de secretária ou num servidor à parte.

## Instalar o Jupyter Notebook
Pressupõe-se que tem uma instalação do Jupyter Notebook a funcionar.

### Instalar um Jupyter Notebook autónomo
Para obter mais informações sobre como instalar localmente um Jupyter Notebook, consulte a [documentação de instalação do Jupyter](https://jupyter.org/install).

### Adicionar ao VS Code
O VS Code também disponibiliza uma extensão que permite executar blocos de notas diretamente no VS Code.  Instale a extensão a partir do [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)


## Instalar os utilitários do PlaidCloud
Embora seja possível aceder ao PlaidCloud com pedidos OAuth e JSON-RPC padrão, recomenda-se a utilização das nossas bibliotecas pré-construídas para um acesso simplificado.  Além disso, a biblioteca de utilitários do PlaidCloud inclui auxiliares de dados práticos para utilizar com DataFrames do Pandas.

Para instalar os utilitários do PlaidCloud, execute as seguintes instalações com pip:

```bash
pip install plaidcloud-rpc@git+https://github.com/PlaidCloud/plaid-rpc.git@v1.4.0#egg=plaidcloud-rpc
```

```bash
pip install plaidcloud-utilities@git+https://github.com/PlaidCloud/plaid-utilities.git@v1.5.2#egg=plaidcloud-utilities
```

## Obter um token OAuth

Consulte [Configuração de OAuth](/pt-pt/reference/cli/jupyter/oauth-setup/) para obter mais informações sobre como obter um token OAuth e como configurar o sistema para autenticação automatizada.


## Abrir a interface de utilizador do Jupyter Notebook

Inicie o servidor de blocos de notas para começar.



Depois de iniciar sessão no servidor de blocos de notas Jupyter, crie um novo bloco de notas a partir da interface.

Será aberto um bloco de notas em branco.



Crie uma ligação para comunicar com o PlaidCloud através dos endpoints da API

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection()
```


Crie um objeto de tabela local e consulte-o, com os resultados colocados automaticamente num DataFrame do [Pandas](https://pandas.pydata.org/).

```python
tbl_sf_cust_master = conn.get_table('Salesforce_Customer_Master') # This gets a table object
df_sf_cust_master = conn.get_data(tbl_sf_cust_master) # This retrieves all the data into a dataframe
```


Com esse mesmo objeto de tabela, também pode escrever consultas mais avançadas com a sintaxe padrão do SQLAlchemy.

```python
df_sf_cust_master_w_sales = conn.get_data(
    tbl_sf_cust_master.select().with_only_columns(
        [tbl_sf_cust_master.c.Id, tbl_sf_cust_master.c.CurrencyIsoCode, tbl_sf_cust_master.c.SyDSalesRegion]
    ).where(
        tbl_sf_cust_master.c.TotalSalesPast3Years > 0
    )
)
```
