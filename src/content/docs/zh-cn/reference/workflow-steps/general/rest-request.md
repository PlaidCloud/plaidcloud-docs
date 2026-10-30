---
title: REST 请求
description: 在工作流步骤中调用 REST API——从 Postman、OpenAPI 或 HAR 导入端点，并将响应路由到表或工作流变量。
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/rest-request.md
---

## 说明

**REST 请求**步骤调用 REST API，并将响应路由到目标表或工作流变量。它以一个统一的 Postman 风格步骤取代了较早的各种 REST 类步骤：选择端点（手动、Postman、OpenAPI/Swagger 或 HAR），编辑标头/查询/正文，发送测试请求，然后保存。

完整的操作演练，请参见 [REST 请求步骤指南](/zh-cn/guides/workflows/rest-request-step/)。

编辑时，浏览器会为该步骤保留一份本地草稿。如果在保存之前关闭或重新加载，重新打开该步骤时会提示恢复这份未保存的草稿。

## 配置

### 请求

* **端点来源**——`Manual`、`From the connection's API definition`、`Postman collection (file/URL)`、`OpenAPI / Swagger (URL/file)` 或 `HAR archive (file)`。使用**加载目录**列出已导入来源的端点；选择其中一个会填入其方法、URL、标头、查询参数和正文，如果您已编辑过请求，则会先询问。三种文件来源还提供**粘贴…**，可让您直接提供集合或规范，而不必选择文件。
* **连接** *（可选）*——用于身份验证和基础 URL 的 REST 连接；省略则直接调用完整 URL。选择器旁的编辑快捷方式会打开所选连接的编辑器以供查看或编辑。
* **方法**——`GET`、`POST`、`PUT`、`PATCH`、`DELETE`、`HEAD`、`OPTIONS`。
* **端点**——路径（有连接时）或完整 URL。
* **标头** / **查询参数**——带开关的名称/值行。
* **正文**——请求负载（JSON、表单或原始内容）。
* **发送测试请求** / **复制为 curl** / **从 curl 导入**——发出请求并在页面内查看响应；复制等效的 curl 命令（机密已隐藏）；或粘贴 curl 命令来填充方法、URL、标头和正文。
* **发送**——`One request`（默认），或 `One request per table row`，即针对驱动因素表逐行展开请求。

在成功执行**发送测试请求**之前保存出站请求的更改，会要求确认。在逐行展开模式下，**测试第 1 行**是消除该警告的成功测试。

当**发送**为 `One request per table row` 时，选择一个**驱动因素表**（用表选择器选取或输入名称），并在端点、查询、标头或正文中使用 `{{row.column}}` 标记来替换每一行的值。端点和正文的变量插入菜单包含所选驱动因素表的列。可选项：**驱动因素筛选器**（SQL `WHERE` 子句）、**关键列**（带到每个输出行）、**行数限制**、**并发数**、**最大请求数/秒**（限制所有工作进程启动请求的速度，与并发数无关；接受小数，因此 0.5 表示每两秒发送一个请求；0 表示不限制；超过 1000 的值会被限制为 1000 并给出警告）、**Add Idempotency-Key header**（在单个无分页的 POST/PUT/PATCH 上为每行发送稳定的 `Idempotency-Key`，使重新运行不会重复创建；否则跳过并给出警告）、**Continue on error**（记录失败的行并发出警告，而不是中止），以及**响应**（默认为 `Parsed records`；`Text (one row per request)` 将每个响应写为一行，带 `DownloadData` 和 `DownloadHeaders` 列；`Raw text, errors as rows` 同样如此，但正文与服务器发送的完全一致，并添加 `DownloadStatus` 列，将 HTTP 或传输错误保留为一行，正文、标头和错误文本中的凭据均已隐藏）。**测试第 1 行**会针对第一个驱动行发出请求，使您可以在运行之前预览展开结果。展开会写入目标表；不能捕获到变量。

当**响应**设为 `Text (one row per request)` 时，还适用另外两个展开选项：

* **响应正文**——`As returned`（默认）；`Visible page text` 在 `DownloadData` 中写入 HTML 页面的可见文本而不是标记；`Raw bytes (Base64)` 将正文的字节与服务器发送的完全一致地以 base64 编码写入，适用于文件或其他二进制响应。
* **响应匹配时持续轮询**——适用于在作业完成前一直回答“仍在处理”的 API。给出一个**响应路径**（`$` 表示整个响应，然后是 `.name`、`[0]`、`['name']` 或 `["name"]`）、一个运算符（`==`、`!=`、`<`、`<=`、`>` 或 `>=`）以及一个带类型的值（`Text`、`Number`、`True/False` 或 `Empty`）。只要响应匹配，就会每隔 **N seconds**（1 到 600，默认 5）重新发送该行的请求，每行最多 **M requests per row**（1 到 1000，默认 60）；最后一次请求之后仍匹配的行会失败。

要发送二进制内容，例如以 base64 文本存储在某列中的文件或音频，请开启**正文为 base64 文本：发送其解码后的字节**（`body_base64`）。使用逐行请求时，正文在填入其 `{{row.column}}` 标记之后，会被当作 base64 文本读取，并发送其解码后的字节。

**文本响应选项**和**登录、代理和 TLS**部分包含以下字段。转换后的 KNIME 工作流也会用到它们。

逐行请求且**响应**设为 `Text (one row per request)` 时：

* **将每个响应的 HTTP 状态添加为 DownloadStatus 列**（`include_status`）——将每个响应的 HTTP 状态添加为 `DownloadStatus` 列。**状态列**（`status_column`）为该列另行命名，设置后即会添加该列。
* **保留失败请求的行，并带 DownloadStatus 和 DownloadError**（`keep_error_rows`）——失败的请求保留其行，正文缺失，并填入 `DownloadStatus` 和 `DownloadError`。
* **保留失败请求的行**（`keep_failed_rows`）——返回 HTTP 400 或更高状态的请求会保留其行，带有状态、响应标头，以及 `DownloadError` 中的错误正文；没有响应的请求只保留其关键列。**Continue on error** 关闭时，失败仍会使步骤停止。**按响应状态使步骤失败**（`fail_on_status`）列出会使步骤失败的状态族，例如 `5xx`；其他状态族的响应会保留为行。
* `document` *（通过 AI 助手或 REST API 设置）*——将每个响应保存为此文档文件夹中的文件，格式为 `{account, path, file_name}`，其中 `file_name` 默认为 URL 的最后一段。该行保存的是 `FilePath`，而不是正文。
* **将正文写为网页文档**（`html_document`）——将每个正文写为规范化的 HTML 文档（`html`）或其 XML 形式（`xml`）。**将相对的 href 和 src 值转为绝对值**（`html_absolute_urls`，默认为 true）会根据请求 URL 将相对的 `href` 和 `src` 值转为绝对值。
* **按第一个成功的响应确定正文列的类型**（`typed_body`）——按第一个成功的响应确定正文列的类型：根据其 `Content-Type` 为 JSON、文本或二进制。之后其他类型的响应、无法解析的 JSON 以及空正文都按缺失处理。
* **为每个响应头添加一列**（`all_headers`）——为每个响应头添加一个文本列，位于状态列之后；响应未发送的头按缺失处理。
* **添加响应 Cookie (DownloadCookies)**（`cookies`）——添加 `DownloadCookies`，即每个响应的 Cookie。

逐行请求时：

* **跳过 URL 不是绝对 http(s) URL 的行**（`skip_invalid_urls`）——URL 不是绝对 HTTP 或 HTTPS URL 的行不发送请求，也不写入行。**某行的 URL 不是绝对 http(s) URL 时使步骤失败**（`fail_invalid_urls`）则会对此类行改为使步骤失败。
* **不发送行值为 NULL 的请求头**（`skip_null_headers`）——`{{row.column}}` 值为 NULL 的请求头不会发送。**某个请求头的行值为 NULL 时使步骤失败**（`fail_null_headers`）则改为使步骤失败。
* **SOAP 操作**（`soap`）——针对端点所指定 WSDL 的某个操作，每行调用一次：`service`、`port` 和 `operation`（留空时各取第一个），`inputs` 将每个参数映射到列或常量，`outputs` 指定要写为列的响应元素（为空时每个叶元素一列），`xml` 用于将响应元素添加为 XML。WSDL 和服务地址必须是公共的 HTTP 或 HTTPS URL。

适用于任何请求：

* **响应 HTTP Digest 质询**（`digest_auth`）——使用连接的基本身份验证用户名和密码响应 HTTP Digest 质询。**响应 NTLM 质询**（`ntlm_auth`）以同样方式响应 NTLM 质询；将用户名写为 `DOMAIN\user` 即可指定域。
* `proxy`——通过 HTTP 或 SOCKS 代理发送请求，由**代理协议**（`protocol`：`http`、`https`、`socks`、`socks4` 或 `socks5`）、**代理主机**（`host`）、**代理端口**（`port`）、**直接发送的主机**（`excluded` 主机模式）和**代理用户名**（`username`）设置。密码是连接的 `proxy_password`，仅当连接的 `proxy_host` 就是该主机时才会使用。

对工作流变量的 `{{name}}` 引用（也可写为 `{{var.name}}` / `{{project_var.name}}`）会在运行时在端点、标头、查询值和正文中被替换。只有双花括号会被替换，因此 JSON 正文中的单花括号保持字面原样。传感器/Webhook 运行还会提供 `{{trigger_sensor_id}}`、`{{trigger_sensor_type}}`、`{{trigger_fired_at}}` 和 `{{trigger_payload_json}}`（非触发的运行中为空）。

编辑器会在端点、标头和查询表以及正文编辑器中高亮显示检测到的 `{{...}}` 标记。

**重试次数**仅适用于幂等方法（GET/HEAD/OPTIONS/DELETE）；POST/PUT/PATCH 始终只发送一次，因此非幂等的正文绝不会被重复发送。**重试次数**接受 0 到 100。**超时（秒）** 是每个请求的限制，范围为 1 到 600 秒；测试请求最多等待 300 秒。有关目录筛选、粘贴和拖放、JSON 工具、请求警告和测试结果，请参见 [REST 请求步骤](/zh-cn/guides/workflows/rest-request-step/)。

### 响应目标位置

* **表** *（默认）*——将响应解析到**目标表**（必填；仅限表，不能是视图）。控件：**行格式**（`Object` 或 `Array`；逐行请求需要 `Object`）、**项路径**、**分页模式**（`No Paging`、`Offset Paging`、`Page Number Paging`、`Next Page URL Paging`、`Cursor Paging` 或 `Link Header Paging (RFC 5988)`）、**模式参数**、**模式路径**、“Dump raw JSON instead of parsing rows”、**重试次数**、**超时（秒）**。**表数据选择**选项卡将响应字段映射到列；**检查源** → Populate 会根据实时响应填充映射，这需要一个连接，并且在发送 GET、HEAD 或 OPTIONS 以外的方法之前会先询问。不提供**汇总**和**非重复**。
* **工作流变量**——发出一个请求，并设置 `{prefix}_status`、`{prefix}_body`、`{prefix}_headers` 和 `{prefix}_elapsed_ms`。**变量前缀**必须是普通标识符，且不能是 `cloud`、`project`、`model`、`date` 之一。

## 行为

* 在变量模式下，步骤只发出一个请求；分页和行解析不适用。
* 捕获的变量可在下游按名称引用，例如 `{my_call_status}`。
