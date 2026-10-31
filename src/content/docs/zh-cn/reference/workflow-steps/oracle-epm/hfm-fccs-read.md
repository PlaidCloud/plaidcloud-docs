---
title: "HFM/FCCS：读取数据（临时）"
description: 在步骤表单中构建视点，自助从 Oracle FCCS 获取数据切片：返回的网格自动落地为表，重复拉取会被缓存，实体列已就绪可用于行级安全，可选的限定目标可将其变为计划的定期加载。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-epm/hfm-fccs-read.md
---

## 描述

通过 [HFM/FCCS 连接](/zh-cn/guides/connections/hfm-fccs/)，按**视点 (POV)** 而非编写查询的方式，从 Oracle **FCCS**（Financial Consolidation and Close，EPM Cloud）读取临时数据切片。财务用户选择应用程序，用 FCCS 维度构建视点，然后运行步骤；返回的网格会自动落地为项目表（读时模式：表根据网格的列创建）。这感觉像实时查询，但在底层，该步骤会向 FCCS 提交导出作业，**轮询**直至完成，然后获取并落地结果，因此耗时较长的切片不会造成阻塞，也无需向 HFM 团队提交工单。

此步骤显示在步骤菜单的 **Oracle EPM (HFM/FCCS)** 下。

:::note[限定实体维度范围]
请将**实体**选择限定在有界范围内：未限定范围的提取可能会在导出作业运行期间长时间锁定 FCCS 应用程序。
:::

## 配置

### 源和目标

| 字段 | 是否必填 | 说明 |
|---|---|---|
| HFM/FCCS 连接 | 是 | 用于读取的 [HFM/FCCS 连接](/zh-cn/guides/connections/hfm-fccs/)。 |
| 环境 | 是 | 连接的环境。 |
| 应用程序 | 是 | 要读取的 FCCS 应用程序。如果设置了连接的默认应用程序，则默认使用它。选择应用程序会驱动视点的实时成员发现。 |
| 目标表 | 是 | 返回的网格落地到的项目表。 |

### 视点

使用 FCCS 维度构建切片。在受支持的 Pod 上，选择连接和应用程序后，成员列表会通过实时元数据发现自动填充；在较旧的 Pod 上，需要手动输入成员名称。

| 维度 | 是否必填 | 说明 |
|---|---|---|
| 方案 | 是 | |
| 年度 | 是 | |
| 期间 | 是 | |
| 实体 | 有界 | 必须指定有界切片：表单会拒绝空选择、“全部”或超过 500 个成员的选择。请保持范围受限，以免导出锁定应用程序。 |
| 科目 | 否 | |
| 自定义 1–自定义 4 | 否 | 应用程序的自定义维度。 |
| ICP | 否 | 公司间。 |
| 视图 | 否 | |
| 值 | 否 | |

未设置的可选维度不会对该轴应用任何筛选（使用 FCCS 的默认成员）。

### 限定目标

默认关闭：每次运行都会落地一个临时切片，并覆盖目标表。

| 字段 | 说明 |
|---|---|
| 限定目标（计划的定期加载） | 勾选后，目标会成为**持久**表：步骤使用键集 upsert 合并到该表而不是覆盖，当后续网格带来新列时，架构会以增量方式扩展（新列只会引发警告，绝不会导致失败）。将该步骤放入计划的工作流，即可得到累积而非清除数据的定期加载。 |
| 关键列 | 仅在开启限定目标时可用。构成合并键的列，以逗号分隔（例如 `Entity, Account`）。**留空**则使用落地网格中存在的视点维度列作为合并键。 |

## 工作原理

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 130" role="img" aria-label="该步骤向 FCCS 提交导出作业，轮询直至完成，获取网格并将其落地为表；重复的视点则改为从缓存的表提供。" style="width:100%;max-width:720px;height:auto;">
<defs><marker id="hf-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="58" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">提交作业</text>
<rect x="150" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="198" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">轮询</text>
<rect x="290" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="338" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">获取网格</text>
<rect x="430" y="46" width="120" height="40" rx="7" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" /><text x="490" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">落地为表</text>
<path d="M106 66 L150 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M246 66 L290 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M386 66 L430 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<text x="198" y="34" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">运行期间…</text>
<rect x="590" y="46" width="120" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="650" y="64" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">重复视点</text><text x="650" y="78" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">从缓存提供</text>
<path d="M550 82 C570 100 630 100 650 88" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" stroke-dasharray="4 3" marker-end="url(#hf-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">一次运行会提交导出作业、轮询、获取网格并落地为表。再次请求相同的视点时，会从已落地的副本提供。</figcaption>
</figure>

作业运行期间，步骤会显示轮询状态。落地后，表根据网格的列创建，无需预先定义架构。

## 缓存

再次请求相同的视点时，会**直接从已落地的表提供**，速度极快，而不会向 FCCS 重新提交导出。运行以应用程序、目标表、视点和**截至**标记（默认为 `latest`）作为键；解析为已落地切片的重复运行会报告表保持原样，而不会重新写入。如果要强制重新提取相同的视点，请更改截至标记。

## 行级安全

落地网格的实体轴会被规范化为名称恰好为 **`Entity`** 的列，因此该表**已就绪可用于行级安全**：管理员可以通过[行访问](/zh-cn/administration/access/managing-security-groups-and-assignments/)对其进行管控，使自助用户只能看到其有权访问的实体。

这是**由管理员控制的管控，而非自动完成**。由于提取是在连接的服务账户下运行的，PlaidCloud 不允许步骤自行声明安全设置。管理员需遵循标准的行访问工作流：

1. 为报表**发布**落地的表。
2. 将 `Entity` 列**声明**为管控属性（默认拒绝）。
3. **批准**首次受管控的写入。
4. **协调**使授权生效。

在管理员完成这些操作之前，该表不会被筛选。参见[管理安全组和分配](/zh-cn/administration/access/managing-security-groups-and-assignments/)。

## 功能限制

| 限制 | 含义 |
|---|---|
| 只读 | 从 FCCS 提取切片。不会写入合并数据、运行合并或回写过账。 |
| 必须有界的实体 | 表单会拒绝空的、“全部”或超过 500 个成员的实体选择，并且单个汇总成员仍可能在服务器端展开，因此请保持切片范围受限。 |
| 较旧 Pod 上需手动输入成员 | 如果 Pod 未公开元数据端点，则成员列表不会自动填充；请手动输入成员名称。 |
| 行级安全由管理员管控 | `Entity` 列已就绪可用于行级安全，但管理员必须先发布、声明、批准首次写入并协调，然后该表才会被筛选。 |

## 相关内容

- [从 HFM / FCCS 提取（指南）](/zh-cn/guides/connections/hfm-fccs/)：完整演练。
- [HFM / FCCS 连接器](/zh-cn/reference/connectors/rest/hfm-fccs/)：连接字段参考。
- [Oracle EPM (HFM / FCCS) 步骤](/zh-cn/reference/workflow-steps/oracle-epm/)
- [管理安全组和分配](/zh-cn/administration/access/managing-security-groups-and-assignments/)
