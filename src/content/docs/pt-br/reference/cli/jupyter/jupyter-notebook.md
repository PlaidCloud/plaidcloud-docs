---
title: Notebooks Jupyter
description: Execute Notebooks Jupyter no PlaidCloud para análise interativa de dados, visualização e fluxos de exploração de dados baseados em Python.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/jupyter-notebook.md
---

Os Notebooks Jupyter e o Jupyter Lab oferecem recursos interativos excepcionais para analisar, explorar, explicar e relatar dados. O PlaidCloud permite usar as informações diretamente em notebooks.

O PlaidCloud fornece o JupyterHub dentro de cada espaço de trabalho do locatário, caso ele esteja ativado para uso. A documentação abaixo ajuda a configurar o Jupyter separadamente em um computador pessoal ou em um servidor separado.

## Instalar o Notebook Jupyter
Isto pressupõe que você já tenha uma instalação funcional do Notebook Jupyter.

### Instalar um Notebook Jupyter autônomo
Para saber mais sobre como instalar um Notebook Jupyter localmente, consulte a [documentação de instalação do Jupyter](https://jupyter.org/install).

### Adicionar ao VS Code
O VS Code também oferece uma extensão que permite executar notebooks diretamente nele. Instale a extensão pelo [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)


## Instalar os utilitários do PlaidCloud
Embora seja possível acessar o PlaidCloud com solicitações OAuth e JSON-RPC padrão, recomendamos que você use nossas bibliotecas pré-construídas para simplificar o acesso. Além disso, a biblioteca de utilitários do PlaidCloud inclui auxiliares de dados práticos para uso com DataFrames do Pandas.

Para instalar os utilitários do PlaidCloud, execute as seguintes instalações com pip:

```bash
pip install plaidcloud-rpc@git+https://github.com/PlaidCloud/plaid-rpc.git@v1.4.0#egg=plaidcloud-rpc
```

```bash
pip install plaidcloud-utilities@git+https://github.com/PlaidCloud/plaid-utilities.git@v1.5.2#egg=plaidcloud-utilities
```

## Obter um token OAuth

Consulte [Configuração do OAuth](/pt-br/reference/cli/jupyter/oauth-setup/) para saber mais sobre como obter um token OAuth e como configurar o sistema para autenticação automatizada.


## Abrir a interface do usuário do Notebook Jupyter

Inicie o servidor de notebooks para começar.



Depois de fazer login no servidor de notebooks Jupyter, crie um novo notebook pela interface.

Isso abrirá um notebook em branco.



Crie uma conexão para se comunicar com o PlaidCloud por meio dos endpoints da API

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection()
```


Estabeleça um objeto de tabela local e consulte-o, com os resultados colocados automaticamente em um DataFrame do [Pandas](https://pandas.pydata.org/).

```python
tbl_sf_cust_master = conn.get_table('Salesforce_Customer_Master') # This gets a table object
df_sf_cust_master = conn.get_data(tbl_sf_cust_master) # This retrieves all the data into a dataframe
```


Com esse mesmo objeto de tabela, você também pode escrever consultas mais avançadas usando a sintaxe padrão do SQLAlchemy.

```python
df_sf_cust_master_w_sales = conn.get_data(
    tbl_sf_cust_master.select().with_only_columns(
        [tbl_sf_cust_master.c.Id, tbl_sf_cust_master.c.CurrencyIsoCode, tbl_sf_cust_master.c.SyDSalesRegion]
    ).where(
        tbl_sf_cust_master.c.TotalSalesPast3Years > 0
    )
)
```
