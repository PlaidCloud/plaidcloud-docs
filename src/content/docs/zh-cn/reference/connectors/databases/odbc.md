---
title: ODBC
description: 在 PlaidCloud 中通过系统 DSN 或 PlaidLink 代理所在机器上的 ODBC 驱动程序设置 ODBC 连接，支持 Windows 或 Linux。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/odbc.md
---

**ODBC（开放式数据库连接）** 通过运行 [PlaidLink 代理](/zh-cn/reference/cli/plaidlink/)的机器上的 ODBC 设置访问数据库。对于没有专用 PlaidCloud 连接器的数据库，可在代理步骤（例如 [Agent Remote Export of SQL Result](/zh-cn/reference/workflow-steps/agent/agent-remote-export-of-sql-result/) 步骤）中使用。创建时，请选择 **ODBC** 作为连接类型。

:::note
ODBC 连接要求代理上的 PlaidLink 版本为 1.2.31 或更高。请参阅[升级](/zh-cn/reference/cli/plaidlink/upgrade/)。
:::

ODBC 连接有两种工作方式：

- **通过 DSN。** 将 **ODBC 驱动程序**留空，并指定代理所在机器上已设置的数据源（DSN）。DSN 保存驱动程序、服务器、数据库以及其他驱动程序设置，**连接属性**可以覆盖这些设置。适用于任何 ODBC 驱动程序。
- **通过驱动程序。** 选择或输入代理所在机器上已安装的 **ODBC 驱动程序**，然后提供服务器和数据库。PlaidCloud 会向驱动程序传递 `Server` 和 `Database` 设置，其后是所有**连接属性**。适用于 Microsoft 的 SQL Server 驱动程序。对于其他驱动程序，包括列表中建议的其他驱动程序，请使用 DSN。

## 上游文档
每种数据库的 ODBC 驱动程序都有各自的设置。无论是创建 DSN 还是编写连接属性，请参阅驱动程序供应商的文档，了解其接受的关键字。

## 在代理所在机器上创建 DSN

在代理运行的机器上将 DSN 设置为系统 DSN，这样无论代理以哪个账户运行都能找到它。

### 在 Windows 上

1. 打开 **ODBC 数据源（64 位）**。
2. 在 **系统 DSN** 选项卡上，添加一个使用该数据库 ODBC 驱动程序的数据源，并输入服务器、数据库以及驱动程序要求的其他设置。
3. 记下**数据源名称**。您需要在连接中输入它。

:::caution
DSN 必须是 64 位的**系统 DSN**。在 Windows 上，代理以服务形式运行，无法识别用户 DSN，也无法识别在 32 位 ODBC 管理器中创建的 DSN。此时步骤会失败，并报错 `ODBC data source '<name>' is not defined on the agent machine`。
:::

### 在 Linux 上

在 Linux 上，代理通过 unixODBC 访问 ODBC。

1. 安装 unixODBC 和该数据库的 ODBC 驱动程序。
2. 检查驱动程序是否已在 `odbcinst.ini` 中注册，以方括号中的名称为准。大多数驱动程序包会在安装时自动注册，`odbcinst -q -d` 可列出已注册的驱动程序。
3. 将数据源添加到系统的 `odbc.ini` 中，作为以 DSN 命名的节。将 `Driver` 设置为已注册的驱动程序名称，并添加服务器、数据库以及驱动程序要求的其他设置：

   ```ini
   [Sales]
   Driver=ODBC Driver 18 for SQL Server
   Server=sales-db.example.com
   Database=Sales
   ```

4. 记下节名称，此处为 `Sales`。您需要在连接中输入它。

`odbcinst -j` 会显示系统 `odbcinst.ini` 和 `odbc.ini` 的位置，通常在 `/etc` 下。位于用户自己的 `~/.odbc.ini` 中的 DSN，只有在代理以该用户身份运行时才能被找到。

### 在容器中

PlaidLink 容器映像包含 unixODBC，但不包含 ODBC 驱动程序。要在 Docker 或 Kubernetes 中运行的代理里使用 ODBC，请基于该映像构建一个安装了驱动程序的新映像，并将包含 DSN 的系统 `odbc.ini` 添加到映像中，或将其挂载到容器中。该映像以 `plaid` 用户运行，因此安装驱动程序时需切换到 `root`，完成后再切换回 `plaid`。

## 配置

### 数据库连接

| 字段 | 必填 | 说明 |
|---|---|---|
| ODBC 驱动程序 | 否 | 留空则通过 DSN 连接。否则填写代理所在机器上已安装的 ODBC 驱动程序名称，须与该机器注册的名称完全一致：在 Windows 上，与 **ODBC 数据源（64 位）** 的**驱动程序**选项卡中列出的名称一致；在 Linux 上，与 `odbcinst.ini` 中的节名称一致。列表提供常用驱动程序，也可输入其他名称。此处仅 Microsoft 的 SQL Server 驱动程序可用。对于其他驱动程序，包括列表提供的其他驱动程序，请留空并使用 DSN。驱动程序名称不能包含花括号或分号。 |
| 数据源名称（DSN）或服务器 | 是 | 未使用驱动程序时，为代理所在机器上系统 DSN 的名称。使用驱动程序时，为数据库服务器的主机名；SQL Server 使用非默认端口时，为 `host,port`。 |
| 数据库 | 使用驱动程序时 | 要打开的数据库。未使用驱动程序时不可用，因为 DSN 自带数据库名称，且保存时会拒绝没有驱动程序的数据库。 |
| 连接属性 | 否 | 驱动程序的其他设置，格式为以 `;` 分隔的 `KEY=value` 键值对。请参阅[连接属性](#连接属性)。 |

连接没有端口字段。对于使用非默认端口的 SQL Server，请将端口以 `host,port` 的形式添加到服务器中，因为 Microsoft 的 SQL Server 驱动程序不接受端口关键字。使用 DSN 时，请在 DSN 中设置端口，或对支持端口的驱动程序使用 `PORT=5433` 之类的属性进行覆盖。

### 连接属性

**连接属性**在两种模式下都会以 ODBC 的书写方式向驱动程序传递 ODBC 设置：

- 使用驱动程序时，它们会添加在连接自身设置之后。可用于驱动程序需要的其他设置，例如用 `ApplicationIntent=ReadOnly` 连接到只读副本。
- 使用 DSN 时，它们会覆盖 DSN 自身的设置，例如 `PORT=5433`，或用于 IBM i 默认库的 `DBQ=MYLIB`。

各键值对以 `;` 分隔，例如 `Encrypt=yes;ApplicationIntent=ReadOnly`。包含 `;` 的值请用花括号括起来，例如 `KEY={first;second}`，花括号内的 `}` 写作 `}}`。关键字会以大写形式传递给驱动程序；ODBC 关键字不区分大小写。

保存时会拒绝：

- 不是 `KEY=value` 键值对的文本，包括未闭合的花括号和没有值的关键字；
- 重复出现的关键字，无论大小写；
- 连接已通过自身字段设置的关键字：`DRIVER`、`DSN`、`SERVER`、`DATABASE`、`UID`、`PWD`、`USER`、`USERID`、`USERNAME` 和 `PASSWORD`；
- `FILEDSN` 和 `SAVEFILE`，它们会让代理从其机器上的文件读取连接设置，或将设置写入文件。

连接列表会隐藏这些属性，因为驱动程序可能在其中接受自己的凭据关键字；连接自身的表单会显示它们。清空该字段即可移除。请在**身份验证凭据**下输入用户和密码。

:::note
**ODBC Driver 18 for SQL Server** 默认会加密连接并检查服务器证书。对于使用自签名证书的服务器，请在属性中添加 `TrustServerCertificate=yes`。
:::

### 身份验证凭据

| 字段 | 说明 |
|---|---|
| 用户 | 用于连接的用户。通过 DSN 时，留空则按 DSN 的设置登录；对于 SQL Server，可在属性中添加 `TRUSTED_CONNECTION=Yes`，以代理自身的账户登录。使用 SQL Server 驱动程序且未指定用户时，连接以代理自身的账户登录：即其 Windows 账户，或 Linux 上的 Kerberos 票据。 |
| 使用单点登录身份验证（无密码，用户可选） | 无需已存储的密码即可连接。 |
| 密码 | 用户的密码（只写）。编辑时留空可保留已保存的密码。 |

### SSL 配置和 SSH 配置

这些选项卡不适用于 ODBC 连接。请在 DSN 或连接属性中设置加密及其他驱动程序选项。

## 早期版本保存的连接

早期版本的此表单要求填写**数据库**并从固定列表中选择驱动程序，还会填入**端口**，但从未将驱动程序传递下去，因此这些连接无法连接。请打开连接，然后任选其一：

- **通过 DSN 连接：** 清空 **ODBC 驱动程序**，输入 DSN 并保存。保存会清除旧的数据库。
- **通过 SQL Server 驱动程序连接：** 检查 **ODBC 驱动程序**是否与代理所在机器上安装的某个 SQL Server 驱动程序匹配。旧列表中的许多名称并不是驱动程序注册时使用的名称。

保留了旧列表中驱动程序的连接会作为驱动程序连接打开。在驱动程序成为代理所在机器上已安装的 SQL Server 驱动程序之前，它无法连接；对于任何其他数据库，请通过 DSN 连接。

保存时也会清除旧的端口。只使用过 DSN、没有数据库的连接，打开时 **ODBC 驱动程序**为空。
