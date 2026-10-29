---
title: Run SAP PCM Hyper Loader 步骤
description: 通过 PlaidCloud 工作流步骤运行 SAP PCM Hyper Loader，将数据高速批量加载到 PCM 模型中。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader.md
---

## 说明


使用直接表加载的方式加载 SAP Profitability and Cost Management (PCM) 模型。此过程明显快于 Databridge。Hyper Loader 几乎支持当前所有 PCM 数据表、分配表和结构表。


以下是当前可用的加载目标：


* 活动别名
* 活动维度层次结构
* 活动动因别名
* 活动动因维度层次结构
* 活动动因值
* BOM 默认构成
* BOM 外部单位费率
* BOM 构成
* BOM 产量
* BOM 销售单位数
* 成本对象 1 别名
* 成本对象 1 维度层次结构
* 成本对象 2 别名
* 成本对象 2 维度层次结构
* 成本对象 3 别名
* 成本对象 3 维度层次结构
* 成本对象 4 别名
* 成本对象 4 维度层次结构
* 成本对象 5 别名
* 成本对象 5 维度层次结构
* 成本对象分配
* 成本对象动因
* 明细项目别名
* 明细项目详情别名
* 明细项目详情维度层次结构
* 明细项目详情值
* 明细项目维度层次结构
* 明细项目直接活动分配
* 明细项目资源动因分配
* 明细项目值
* 期间别名
* 期间维度层次结构
* 资源动因别名
* 资源动因维度层次结构
* 资源动因拆分
* 资源动因值
* 责任中心别名
* 责任中心维度层次结构
* 收入
* 收入别名
* 收入维度层次结构
* 服务别名
* 服务维度层次结构
* 分摊别名
* 分摊维度层次结构
* 分摊值
* 版本别名
* 版本维度层次结构
* 工作表 1 别名
* 工作表 1 维度层次结构
* 工作表 2 别名
* 工作表 2 维度层次结构
* 工作表值

## 我们的资质


PlaidCloud 是 SAP 官方合作伙伴，也是 SAP PCM 模型设计与实施相关服务的首选供应商。


## 保存时的检查内容

**加载步骤**选项卡上的每个源都会按列名匹配，暂存到为其选择的**目标加载表**所对应的加载器表中。出现以下情况时，保存会被拒绝，并指明相关的源：

- 源没有目标加载表，或所选的表不是 PCM 加载器表——*Source 'activity_aliases' loads into 'ACTIVITY', which isn't a PCM loader table.*
- 源的列与其加载器表不匹配：加载器表的某一列缺失、类型与加载器表中的不同，或没有源、表达式或常量——*Source 'activity_aliases' doesn't match loader table PPLOAD_ACTIVITY_AL: missing DEFAULTALIAS; no source, expression or constant for ALIAS.* **将目标列重置为架构**会根据加载器表重新填充源的目标列。
- 两个源同名。每个源都会导出为以其名称命名的文件，因此其中一个会覆盖另一个——*Source name 'activity_aliases' is used more than once; each source needs its own, or one overwrites the other.*


## 示例


从下拉列表中选择“要使用的代理”。输入模型名称并选择加载包的存储路径位置，然后从中选择所需的子文件夹。使用下方的“表数据选择”来选择源表模型和目标加载表。检查源 >> 传播两侧的表即可显示数据。输入数据并添加所需的表达式后，单击“Save and Run Step”。
