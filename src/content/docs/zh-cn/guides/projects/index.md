---
title: 项目
description: 设置和管理 PlaidCloud 项目，按用途组织工作流、表、数据导入和其他分析对象。
sidebar:
  label: 项目
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/index.md
---

**项目**是 PlaidCloud 中的工作单元。每个项目拥有各自的数据、工作流、维度和审计历史。项目之间不共享状态——它们相互隔离，因此自然成为区分不同分析、业务流程或数据产品的边界。

大多数团队从每个分析领域一个项目开始：一个项目用于人员成本分摊，另一个用于收入分析，再一个用于月度结账——怎么贴合团队看待自身工作的方式就怎么划分。

## 本节内容

- [管理项目](/zh-cn/guides/projects/managing-projects/)——在工作区中创建、配置和组织项目
- [Data Foundation：Common Finance Model](/zh-cn/guides/projects/data-foundation/)——通过直接连接，将来自多个 ERP 系统和实例的 ERP 数据整合到一个 Common Finance Model 中，供报表、指标和 AI 助手统一读取
- [Data Foundation 入门](/zh-cn/guides/projects/data-foundation-getting-started/)——从新建项目到已加载、已检查、已移交模型的设置清单
- [Cost to Serve](/zh-cn/guides/projects/cost-to-serve/)——按活动将运营费用分摊到客户，并查看扣除服务成本后的利润
- [Operational Transfer Pricing](/zh-cn/guides/projects/operational-transfer-pricing/)——根据您的政策区间检验各实体的利润水平，并查看补差
- [查看项目](/zh-cn/guides/projects/viewing-projects/)——查找并打开现有项目
- [管理层次结构](/zh-cn/guides/projects/managing-hierarchies/)——用于组织大量项目的文件夹结构
- [管理表和视图](/zh-cn/guides/projects/managing-tables-and-views/)——项目内部的数据层
- [管理数据编辑器](/zh-cn/guides/projects/managing-data-editors/)——谁可以修改项目数据
- [查看项目日志](/zh-cn/guides/projects/viewing-the-project-log/)——变更的审计跟踪
- [归档项目](/zh-cn/guides/projects/archive-a-project/)——保留已完成的工作而不删除
- [面包屑导航和链接](/zh-cn/guides/projects/breadcrumbs-and-shareable-links/)——从任意窗口向上返回，并分享指向当前所见内容的链接
- [比较和合并项目](/zh-cn/guides/projects/compare-and-merge-projects/)——对比两个项目，并有选择地在它们之间复制更改
- [导出为可移植格式](/zh-cn/guides/projects/export-to-portable-format/)——将项目打包为可在平台之外运行的独立 Python + DuckDB 程序
- [管理存储](/zh-cn/guides/projects/managing-storage/)——查看工作区存储了什么，并设置表保留历史的时长
- [使用标签组织工作](/zh-cn/guides/projects/organizing-with-labels/)——为工作流、步骤、表和其他对象添加标签，以便分组和筛选
- [共享链接](/zh-cn/guides/projects/sharing-links/)——从地址栏复制链接，直接打开项目、工作流、表或维度

## 相关内容

- [概念](/zh-cn/get-started/concepts/)——项目与工作区、成员以及更广泛的数据模型之间的关系
- [工作流](/zh-cn/guides/workflows/)——存在于项目内部的自动化基本单元
- [访问管理](/zh-cn/administration/access/)——决定谁可以查看和编辑项目的工作区级控制
