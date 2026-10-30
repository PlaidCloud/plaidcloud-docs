---
title: Jupyter 笔记本
description: 在 PlaidCloud 中运行 Jupyter 笔记本，进行交互式数据分析、可视化以及基于 Python 的数据探索工作流。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/jupyter-notebook.md
---

Jupyter 笔记本和 Jupyter Lab 提供出色的交互能力，可用于分析、探索、解释和报告数据。PlaidCloud 支持直接在笔记本中使用信息。

如果已启用，PlaidCloud 会在每个租户工作区内提供 JupyterHub。以下文档帮助您在桌面或独立服务器上单独设置 Jupyter。

## 安装 Jupyter 笔记本
此处假设您已有可用的 Jupyter 笔记本安装。

### 安装独立的 Jupyter 笔记本
有关在本地安装 Jupyter 笔记本的更多信息，请参阅 [Jupyter 的安装文档](https://jupyter.org/install)。

### 添加到 VS Code
VS Code 也提供一个扩展，可让您直接在 VS Code 中运行笔记本。请从 [Visual Studio Marketplace](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter) 安装该扩展。


## 安装 PlaidCloud 实用工具
虽然可以使用标准 OAuth 和 JSON-RPC 请求访问 PlaidCloud，但建议使用我们预构建的库以简化访问。此外，PlaidCloud 实用工具库还包含便于配合 Pandas DataFrame 使用的数据辅助工具。

要安装 PlaidCloud 实用工具，请执行以下 pip 安装命令：

```bash
pip install plaidcloud-rpc@git+https://github.com/PlaidCloud/plaid-rpc.git@v1.4.0#egg=plaidcloud-rpc
```

```bash
pip install plaidcloud-utilities@git+https://github.com/PlaidCloud/plaid-utilities.git@v1.5.2#egg=plaidcloud-utilities
```

## 获取 OAuth 令牌

有关如何获取 OAuth 令牌以及如何配置系统以实现自动认证，请参阅 [OAuth 设置](/zh-cn/reference/cli/jupyter/oauth-setup/)。


## 打开 Jupyter 笔记本用户界面

启动笔记本服务器即可开始。



登录 Jupyter 笔记本服务器后，从界面中创建一个新笔记本。

这将打开一个空白笔记本。



创建连接，通过 API 端点与 PlaidCloud 通信

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection()
```


建立本地表对象并对其进行查询，结果会自动放入 [Pandas](https://pandas.pydata.org/) DataFrame 中。

```python
tbl_sf_cust_master = conn.get_table('Salesforce_Customer_Master') # This gets a table object
df_sf_cust_master = conn.get_data(tbl_sf_cust_master) # This retrieves all the data into a dataframe
```


使用同一个表对象，还可以用标准 SQLAlchemy 语法编写更高级的查询。

```python
df_sf_cust_master_w_sales = conn.get_data(
    tbl_sf_cust_master.select().with_only_columns(
        [tbl_sf_cust_master.c.Id, tbl_sf_cust_master.c.CurrencyIsoCode, tbl_sf_cust_master.c.SyDSalesRegion]
    ).where(
        tbl_sf_cust_master.c.TotalSalesPast3Years > 0
    )
)
```
