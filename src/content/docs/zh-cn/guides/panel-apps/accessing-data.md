---
title: 读取数据和已登录用户
description: 以查看者的身份将服务器端 Panel 应用连接到 PlaidCloud：读取项目数据，并使用查看者的身份实现按用户定制的行为和行级安全。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/accessing-data.md
---

服务器 Panel 应用可以读取您的 PlaidCloud 数据，并且是 **以查看者的身份** 读取。有人打开应用时，PlaidCloud 会使用与平台其他部分相同的单点登录让其登录，应用发出的每次调用都使用 **该查看者自己的权限** 运行。不存在共享的服务账户，应用也永远看不到查看者自己无权查看的数据。

这仅适用于 **服务器** 应用。WASM 应用完全在浏览器中运行，没有服务器端连接。

## 连接到 PlaidCloud

使用 `PlaidConnection`，并指定要读取数据的项目：

```python
from plaidcloud.utilities.connect import PlaidConnection

conn = PlaidConnection(project_id="<your-project-id>")
```

这就是全部设置。您 **无需** 提供令牌、用户名或密码，连接会自动以已登录的查看者身份进行身份验证。项目 id 可在项目的 URL 或设置页面中找到。

> **为应用指定项目。** 在 **项目** 选择器中选择了项目并发布的应用，默认读取该项目，[数据 API](/zh-cn/guides/panel-apps/data-api/) 也会将其用于 `table("name")`。对于没有项目的应用，请如上所示向 `PlaidConnection` 传入 `project_id`；单独的 `PlaidConnection()` 没有可读取的项目。

### 读取表

有了连接后，即可按名称将表提取到 pandas DataFrame 中：

```python
df = conn.get_dataframe("Sales Ledger")
```

由于连接就是查看者本人，因此它只返回查看者有权查看的行；如果查看者完全无权访问该项目，则会引发权限错误。

> **按名称读取表，而不是编写 SQL。** 在管理员已启用[行访问](/zh-cn/administration/access/managing-security-groups-and-assignments/#行访问与您自己编写的查询)的项目中，按名称读取会应用每位查看者的行授权，而应用自行组合的查询会被拒绝，除非用户是项目架构师，因为没有单一的表可供授权进行筛选。按名称读取可让应用在两种情况下都正常工作。

## 识别查看者

若要根据 **谁在查看应用** 来调整显示的内容，例如个性化问候语、隐藏选项卡或实现行级安全，请从 Panel 读取已登录的用户：

```python
import panel as pn

viewer = pn.state.user          # the viewer's email address
token  = pn.state.access_token  # their JWT, if you need claims or group membership
```

`pn.state.user` 是查看者的电子邮件，取自其经过验证的登录信息，可以将其作为身份信任。`pn.state.access_token` 是其原始访问令牌，在需要解码分组或角色声明以制定更细粒度的规则时很有用。

### 行级安全

将两者结合：读取查看者，然后按查看者筛选每个查询。例如，只向每位区域经理显示其所在区域：

```python
import panel as pn
from plaidcloud.utilities.connect import PlaidConnection

pn.extension()

viewer = pn.state.user
conn = PlaidConnection(project_id="<your-project-id>")

sales = conn.get_dataframe("Regional Sales")
mine = sales[sales["manager_email"] == viewer]

pn.Column(
    f"# Sales for {viewer}",
    pn.pane.DataFrame(mine, index=False),
).servable()
```

由于连接已经强制执行查看者的项目权限，因此这种筛选是在其可见范围之上的 *额外* 调整，而不能替代 PlaidCloud 自身的访问控制。

> **从应用的主流程发起数据调用。** 在应用代码为查看者的会话运行时（即执行 `.servable()` 的位置），可以获取已登录的查看者。如果要将阻塞调用放到后台线程，请使用 `asyncio.to_thread`：原始线程池不会携带会话的身份，连接会明确报错，而不会读取错误的数据。

## 公共应用

如果发布时选择了 **允许公共访问**，应用无需登录即可提供服务，因此没有可代表的查看者：`pn.state.user` 为空，`PlaidConnection()` 也没有可供验证的对象。请让公共应用只使用对任何人都安全的数据，或者关闭公共访问，让查看者登录并适用上述按用户的模型。
