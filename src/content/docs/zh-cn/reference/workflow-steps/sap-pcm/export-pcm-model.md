---
title: Calculate and Export PCM Model 步骤
description: 通过 PlaidLink 代理运行 PCM 模型计算，并将结果导出到数据库或分隔文件。
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap-pcm/export-pcm-model.md
---

## 说明

通过可访问 PCM 安装的 [PlaidLink 代理](/zh-cn/reference/workflow-steps/agent/)，在一个步骤中计算 SAP PCM 模型并导出结果。[Calculate PCM Model 步骤](/zh-cn/reference/workflow-steps/sap-pcm/calculate-pcm-model/)只运行计算，而此步骤还会移动输出。

## 配置

### 要使用的代理

可访问 PCM 安装的 PlaidLink 代理。

### 模型信息

- **Model name**：要计算的 PCM 模型。
- **Export specification path**：描述要导出内容的 PCM 导出规范。

### 导出输出目标

选择数据库目标、文件目标，或两者都选。

**写入数据库**：默认开启；导出通过规范中配置的数据库目标写入。

**写入文件**：默认关闭。开启后：

- **文件路径**：代理写入文件的位置。
- **别名**：导出中记录的别名。默认为 `DEFAULT ALIAS`。
- **Precision**：导出值的小数位数。默认为 0。
- **分隔符**：逗号、制表符、竖线、分号、空格、`@`、`~` 或 `:`。默认为制表符。
- **追加**：默认关闭，因此每次运行都会替换该文件。开启后可累积多次运行的结果。
- **Include rules**：默认关闭。开启后会将模型的规则与值一起导出。
- **Unicode**：默认关闭。当导出的数据包含默认编码之外的字符时开启。

## 相关内容

- [SAP-PCM 步骤](/zh-cn/reference/workflow-steps/sap-pcm/)
- [Calculate PCM Model 步骤](/zh-cn/reference/workflow-steps/sap-pcm/calculate-pcm-model/)
- [Run SAP PCM Hyper Loader 步骤](/zh-cn/reference/workflow-steps/sap-pcm/run-sap-pcm-hyper-loader/)
