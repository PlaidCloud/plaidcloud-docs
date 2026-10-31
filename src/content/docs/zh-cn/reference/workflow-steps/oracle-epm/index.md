---
title: Oracle EPM (HFM / FCCS) 步骤
description: 通过 HFM/FCCS 连接自助从 Oracle FCCS 获取临时数据切片的工作流步骤：构建视点、运行并将结果落地为表。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-epm/index.md
---

通过 [HFM/FCCS 连接](/zh-cn/guides/connections/hfm-fccs/)从 Oracle **FCCS**（Financial Consolidation and Close，EPM Cloud）读取数据的工作流步骤。财务用户在步骤表单中构建视点并运行，返回的网格会自动落地为项目表，无需向 HFM 团队提交工单，也不需要合并方面的知识。

## 步骤

- [HFM/FCCS：读取数据（临时）](/zh-cn/reference/workflow-steps/oracle-epm/hfm-fccs-read/)：通过视点选择器自助获取数据切片；缓存重复拉取，已就绪可用于行级安全，并可升级为计划的定期加载。

## 相关内容

- [从 HFM / FCCS 提取（指南）](/zh-cn/guides/connections/hfm-fccs/)
- [HFM / FCCS 连接器](/zh-cn/reference/connectors/rest/hfm-fccs/)
