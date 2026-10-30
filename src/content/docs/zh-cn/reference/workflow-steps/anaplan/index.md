---
title: Anaplan 步骤
description: 通过 Anaplan 连接从 Anaplan 读取数据的工作流步骤：已保存的视图、已有的导出操作，或加载到 PlaidCloud 维度中的一个或多个列表，均为云直连。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/anaplan/index.md
---

通过 [Anaplan 连接](/zh-cn/guides/connections/anaplan/)从 **Anaplan** 读取数据的工作流步骤：通过大容量读取请求路径读取已保存的视图，通过 Bulk API 运行已有的导出操作，或将一个或多个列表加载到 PlaidCloud 维度中。这些步骤以**云直连**方式通过 Integration API 访问 Anaplan，不提供本地代理路径，且都不会向 Anaplan 写回数据。

## 步骤

- [Anaplan：读取视图](/zh-cn/reference/workflow-steps/anaplan/anaplan-read-view/)：按保存时的原样读取已保存的视图。云直连。
- [Anaplan：读取导出](/zh-cn/reference/workflow-steps/anaplan/anaplan-read-export/)：运行已有的导出操作并载入其文件。云直连。
- [Anaplan：读取列表](/zh-cn/reference/workflow-steps/anaplan/anaplan-read-list/)：将一个或多个列表读取到 PlaidCloud 维度中。云直连。

## 相关内容

- [连接到 Anaplan（指南）](/zh-cn/guides/connections/anaplan/)
