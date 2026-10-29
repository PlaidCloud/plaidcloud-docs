---
title: User Defined Transform 步骤
description: 在 PlaidCloud 工作流步骤中使用 Python 代码创建自定义数据转换，实现灵活而强大的数据处理逻辑。
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/user-defined-transform.md
---

## 说明

PlaidCloud 自带的**标准工作流转换**通常几乎能完成您需要的所有操作。此外，这些标准转换会持续优化性能，并能提供最可靠的数据。但是，当单独或组合使用标准选项仍无法实现目标时，您可以创建**用户定义转换**来满足需求。PlaidCloud 支持使用标准 Python 代码，包括许多高级软件包。

创建用户定义转换需要使用 Python 编程，其运行于 Python 3.14。如需更多信息，请访问 [Python 网站。](https://www.python.org/)



## 用户定义转换

创建用户定义函数 (UDF) 有两种方式：
 - 直接在 PlaidCloud 中编写和维护逻辑
 - 连接到 Git 仓库并指向某个文件

除了使用标准 Python 外，所有 PlaidCloud API 函数都可直接使用，以便与 PlaidCloud 原生交互。SciPy、PySpark、Pandas 等高级分析软件包均可直接导入。

### 编写并维护存储在 PlaidCloud 中的 UDF
要创建新的用户定义函数 (UDF)，请打开需要自定义转换的工作流，选择**用户定义**选项卡，然后单击 **Add User Defined Function** 按钮。为 UDF 指定一个 ID。创建后，选择“编辑函数逻辑”图标（最左侧），打开“Edit User Defined Function”窗口。

或者，也可以使用**用户定义**选项卡中的**导入**按钮导入以前创建的用户定义函数。只需单击该按钮，然后从下拉菜单中选择相应的工作流（此菜单包含当前工作区内的所有工作流）。接下来，选择要导入的函数，然后单击 **Import Selected Functions** 按钮。

创建/导入函数后，转到工作流的 **Analyze Steps** 选项卡，在适当位置添加 **User Defined Transform** 步骤，就像添加**标准转换**一样。在配置窗口中，选择**分析 UDF**作为类型，然后从下拉菜单中选择相应的**用户定义函数**。

### 引用 Git 仓库中的 UDF

首先，您需要在**外部数据连接**区域创建到 Git 仓库（例如 Github、Gitlab 等）的连接。

Git 仓库连接可用后，转到工作流的 **Analyze Steps** 选项卡，在适当位置添加 **User Defined Transform** 步骤，就像添加**标准转换**一样。在配置窗口中，选择**外部源代码仓库**作为类型，然后选择该 UDF 的连接、分支和**文件路径**。分支选择也支持选择标签，以便实现标准发布流程。

对 Git 中文件的更改会在下次执行 UDF 时自动生效。

## 源表和目标表的配置
虽然可以不在 UDF 转换配置中定义表而直接在 UDF 中访问表，但这样表依赖关系将不可用。因此，建议在配置中定义 UDF 使用的所有源表和目标表。在配置中定义表还能让它们在 UDF 中以更直接的方式随时可用（见下文）。

## 其他变量的指定
项目级和工作流级变量都可通过标准 API 方法在 UDF 中使用，但通常还有一些特定于步骤的其他变量也很有用。这些变量可以在配置的**其他变量**部分中定义。

变量值可以手动设置，也可以结合项目变量和工作流变量动态定义。

## Python UDF 示例

### 常用导入与 PlaidCloud API 连接设置

```python
### COMMON PYTHON IMPORTS
# import os
# import pandas as pd
# import numpy as np

### COMMON PLAIDCLOUD IMPORTS
from plaidcloud.utilities.connect import PlaidConnection
from plaidcloud.utilities import frame_manager as fm
# from plaidcloud.utilities import data_helpers as dh

conn = PlaidConnection()
```

### 在应用程序日志中设置日志消息
```python
conn.logger.info('Sample Info Log Message')
conn.logger.warn('Sample Warning Log Message')
conn.logger.error('Sample Error Log Message')
```

### 访问项目变量和工作流变量
```python
workflow_vars = conn.analyze.workflow.variable_values(project_id=conn.project_id, workflow_id=conn.workflow_id)
variable_1 = workflow_vars.get('my_wf_var_1')

project_vars = conn.analyze.project.variable_values(project_id=conn.project_id)
variable_2 = project_vars.get('my_prj_var_2')
```

### 将数据保存到表
此示例假定数据已存在于 Pandas 数据框中。

```python
fm.save(dfImport, name='/path_to_table/OUTBOUND_TABLE_NAME', append=False)
```

### 从表读取数据

要使用某个表，首先需要获取表对象。获得对象后，即可使用 `get_data()` 方法查询它。`get_data()` 方法还支持 SQLAlchemy 语法，以实现高级查询构建功能。查询结果是 Pandas 数据框对象。

```python
tbl_object = conn.get_table('INBOUND_TABLE_NAME')
dfImport = conn.get_data(tbl_object)
dfImportQuery = conn.get_data(
    tblImport.select().with_only_columns(
        [tblImport.c.Col1, tblImport.c.Col2]
    ).where(
        tblImport.c.Col1 == 'FilterValue'
    )
)
```

### 访问已定义的源表和目标表中的数据
使用在步骤配置中配置的已定义源表和目标表时，初始的对象获取（即 `get_table()`）会自动执行。使用预先配置的表时，流程如下：

```python
# Source Tables as a dict
my_source = conn.udf.source_by_name('my_table')

# All sources as a list
my_sources = conn.udf.sources()

# Target Tables as a dict
my_target = conn.udf.target_by_name('my_table')

# All targets as a list
my_targets = conn.udf.targets()
```

### 访问步骤变量
访问步骤配置中定义的变量，流程如下：

```python
# Access variables by name
my_var = conn.udf.variable_by_name('my_var')

# All variables as a list
my_vars = conn.udf.variables()
```

### 从 Document 读取文件
使用 PlaidCloud 连接访问 Document 中的文件同样很简单。下面是一个函数示例，它获取文件内容并将其保存到运行时容器中的本地路径。

```python
def get_from_document(conn, document_account, remote_path, local_file_path):
    # accounts = conn.document.view.shared_accounts()
    remote_file = base64.b64decode(
        conn.document.view.download(
            account_id=document_account,
            path=remote_path,
        )
    )
    with open(local_file_path, 'wb') as output_file:
        output_file.write(remote_file)

    return local_file_path
```
