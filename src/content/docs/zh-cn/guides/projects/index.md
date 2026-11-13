---
title: 项目
description: 设置和管理 PlaidCloud 项目，按用途组织工作流、表、数据导入及其他分析对象。
sidebar:
  label: 项目
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/index.md
---

**项目**是 PlaidCloud 中的工作单元。每个项目拥有自己的数据、工作流、维度和审计历史。项目之间不共享状态，彼此隔离，因此天然适合作为区分不同分析、业务流程或数据产品的边界。

大多数团队从每个分析领域一个项目开始：一个项目用于人员成本分摊，另一个用于收入分析，还有一个用于月度结账，以贴合团队思考工作的方式为准。

## 本节内容

- [管理项目](/zh-cn/guides/projects/managing-projects/) — 在工作区中创建、配置和组织项目
- [Data Foundation：Common Finance Model](/zh-cn/guides/projects/data-foundation/) — 通过直接连接，将来自多个 ERP 系统和实例的 ERP 数据汇入一个 Common Finance Model，供报表、指标和 AI 代理统一读取
- [Data Foundation 入门](/zh-cn/guides/projects/data-foundation-getting-started/) — 从新建项目到加载、检查并交付模型的设置清单
- [Cost to Serve](/zh-cn/guides/projects/cost-to-serve/) — 按作业将运营费用分摊给客户，并查看扣除服务成本后的利润
- [Operational Transfer Pricing](/zh-cn/guides/projects/operational-transfer-pricing/) — 对照政策区间检验各实体的利润水平，并查看补差结果
- [数据模型与项目元素](/zh-cn/guides/projects/data-model/) — 将表共享的列一次性描述，并查看哪些表共享它
- [项目主页](/zh-cn/guides/projects/project-home/) — 一览项目概况，并管理其变量、计划、访问权限、数据默认值和应用
- [查看项目](/zh-cn/guides/projects/viewing-projects/) — 查找并打开现有项目
- [管理层次结构](/zh-cn/guides/projects/managing-hierarchies/) — 用于组织大量项目的文件夹结构
- [管理表和视图](/zh-cn/guides/projects/managing-tables-and-views/) — 项目内部的数据层
- [管理数据编辑器](/zh-cn/guides/projects/managing-data-editors/) — 谁可以修改项目数据
- [查看项目日志](/zh-cn/guides/projects/viewing-the-project-log/) — 更改的审计跟踪
- [归档项目](/zh-cn/guides/projects/archive-a-project/) — 保留已完成的工作而不删除
- [面包屑导航和链接](/zh-cn/guides/projects/breadcrumbs-and-shareable-links/) — 从任意窗口向上返回，并分享当前所查看内容的链接
- [比较和合并项目](/zh-cn/guides/projects/compare-and-merge-projects/) — 比较两个项目，并有选择地在它们之间复制更改
- [导出为可移植格式](/zh-cn/guides/projects/export-to-portable-format/) — 将项目打包为可在平台外运行的独立 Python + DuckDB 程序
- [管理存储](/zh-cn/guides/projects/managing-storage/) — 查看工作区存储的内容，并设置表保留历史的时长
- [使用标签组织工作](/zh-cn/guides/projects/organizing-with-labels/) — 为工作流、步骤、表和其他对象添加标签，以便分组和筛选
- [分享链接](/zh-cn/guides/projects/sharing-links/) — 从地址栏复制链接，直接打开项目、工作流、表或维度

## 相关内容

- [概念](/zh-cn/get-started/concepts/) — 项目与工作区、成员以及更广泛数据模型之间的关系
- [工作流](/zh-cn/guides/workflows/) — 位于项目内部的自动化基本单元
- [访问管理](/zh-cn/administration/access/) — 控制谁可以查看和编辑项目的工作区级设置
