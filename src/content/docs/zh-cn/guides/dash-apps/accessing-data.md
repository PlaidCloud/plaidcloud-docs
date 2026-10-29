---
title: 在 Dash 应用中读取数据和已登录用户
description: 以查看者的身份将 Dash 应用连接到 PlaidCloud，读取项目数据，并利用查看者的身份实现按用户的行为和行级安全。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dash-apps/accessing-data.md
---

Dash 应用可以读取您的 PlaidCloud 数据，并且是**以查看者的身份**读取，与服务器 Panel 应用完全一样。有人打开应用时，PlaidCloud 会使用平台其他部分所用的同一单点登录让其登录，应用发出的每次调用都以**该查看者自己的权限**运行。不存在共享的服务账户，应用也永远无法看到查看者自己看不到的数据。

辅助函数位于 `plaidcloud_dash` 中，它是 Dash 基础镜像的一部分：

```python
from plaidcloud_dash import current_user, get_connection
```

## 连接到 PlaidCloud

在 Dash 回调内部调用 `get_connection()`，并指定要读取其数据的项目：

```python
from plaidcloud_dash import get_connection

conn = get_connection(project_id="<your-project-id>")
```

这就是全部所需的设置。无需提供令牌、用户名或密码，`get_connection()` 会使用已登录查看者当前会话中的访问令牌，自动以该查看者的身份进行身份验证。项目 ID 可在项目的 URL 或其设置页面中找到。

> **请在回调内部调用。** `get_connection()` 从当前请求的 Flask 会话中读取查看者的令牌，而该会话仅在回调处理该查看者的请求期间可用。如果将阻塞调用放到后台线程中，原始线程池不会携带该会话，请在回调内部读取令牌并显式传入。在请求之外（或在禁用身份验证的情况下）调用 `get_connection()` 会引发 `RuntimeError`，而不是悄悄返回一个没有任何身份的连接。

> **在代码中指定项目。** 发布对话框中没有项目设置，Dash 应用会读取您在 `get_connection(project_id=...)` 中指定的项目，这与服务器 Panel 应用的 `PlaidConnection(project_id=...)` 相同，参见[读取数据和已登录用户](/zh-cn/guides/panel-apps/accessing-data/)。如果应用从不接触项目数据（例如只调用 `current_user()`），可以使用不带 `project_id` 的 `get_connection()`；但如果在没有真实且可访问的项目 ID 的情况下对该连接调用项目级操作，则会引发 `Project Id has not been set`。（如需读取多个项目，请为每个项目打开一个连接。）

### 读取表

有了连接之后，可以按名称将表读入 pandas DataFrame：

```python
df = conn.get_dataframe("Sales Ledger")
```

由于该连接就是查看者本人，因此只会返回查看者有权查看的行；如果查看者完全没有该项目的访问权限，则会引发权限错误。

> **请按名称读取表，而不是编写 SQL。** 在管理员已启用[行访问](/zh-cn/administration/access/managing-security-groups-and-assignments/#行访问与您自己编写的查询)的项目中，按名称读取会应用每位查看者的行授权，而应用自行组合的查询会被拒绝（项目架构师除外），因为没有一个单一的表可供授权进行筛选。按名称读取可以让应用在两种情况下都正常工作。

## 在回调中读取，切勿在导入时或进程范围内读取

一个进程为所有查看者提供服务。要做好数据隔离，归结起来是两条规则：

- **切勿在模块范围（导入时）打开连接或读取表。** 您的 `app.py` 及其导入的所有模块只会在容器启动时运行**一次**，此时还没有人登录。在那里调用 `get_connection()` 或 `PlaidConnection()` 没有可供验证身份的查看者，会导致应用在启动时失败（这是“应用无法启动”崩溃循环最常见的原因）。请把所有读取都放在回调内部，那里有查看者的请求及其会话令牌。

- **切勿在模块或进程范围缓存按查看者区分的结果。** 带线程的 gunicorn 工作进程会在所有并发查看者之间共享同一个 Python 进程，因此存放在模块级变量、全局字典或 `lru_cache` 中的 DataFrame 对*所有*其他查看者可见，一个人的行会泄露到另一个人的视图中。请在回调内部计算按查看者区分的数据，并在回调返回时让其离开作用域：

  ```python
  # WRONG — a module/process-global cache is shared across all viewers
  _CACHE = {}

  @app.callback(...)
  def _load(n):
      viewer = current_user()
      if viewer not in _CACHE:                      # still process-global; leaks under load
          _CACHE[viewer] = get_connection(project_id="…").get_dataframe("Sales")
      return _CACHE[viewer].to_dict("records")

  # RIGHT — read inside the callback, no shared state
  @app.callback(...)
  def _load(n):
      conn = get_connection(project_id="…")          # this viewer, this request
      return conn.get_dataframe("Sales").to_dict("records")
  ```

### 共享参考数据

如果多位查看者确实需要*相同*的参考数据（例如查找表或产品列表），不要试图通过进程级缓存来共享。请通过 PlaidCloud 常规的[行访问/项目权限](/zh-cn/administration/access/managing-security-groups-and-assignments/)将这些表授权给应用的用户，让每位查看者在各自的 `get_connection()` 下读取。每个人得到相同的参考行，是因为他们被授予了相同的访问权限，而不是因为复用了某位查看者的读取结果。

## 识别查看者

如需根据**谁在查看**来定制应用显示的内容（例如个性化问候、隐藏选项卡或行级安全），请调用 `current_user()`：

```python
from plaidcloud_dash import current_user

viewer = current_user()  # the viewer's identifier
```

`current_user()` 返回已登录查看者的标识符，即其用户名；如果没有用户名声明，则依次回退到电子邮件和账户 ID。该标识符取自经过验证的登录，因此可以将其作为其身份信任。它不会引发异常；在禁用身份验证或请求之外调用时，返回空字符串。

### 行级安全

将两者结合：先读取查看者，然后用其筛选每个查询。例如，只向每位区域经理显示其所在的区域：

```python
from dash import Input, Output
from plaidcloud_dash import current_user, get_connection


@app.callback(Output("sales-table", "children"), Input("load-btn", "n_clicks"))
def _load_my_region(n_clicks):
    viewer = current_user()
    conn = get_connection(project_id="<your-project-id>")

    sales = conn.get_dataframe("Regional Sales")
    mine = sales[sales["manager_email"] == viewer]

    return mine.to_dict("records")
```

由于连接本身已经强制执行查看者的项目权限，这里的筛选是在其可见范围之上进行的*额外*整理，而不能替代 PlaidCloud 自身的访问控制。

## 公共应用

如果发布时选择了**允许公共访问**，应用无需登录即可提供服务，因此没有可代表的查看者：`current_user()` 返回空字符串，`get_connection()` 没有可用于身份验证的会话令牌，因此会引发异常。请让公共应用只使用任何人都可安全查看的数据，或者关闭公共访问，让查看者登录并适用上述按用户的模型。
