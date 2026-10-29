---
title: 运行应用操作
description: 在工作流中调用已注册的应用程序操作，可选择传入文档路径和参数。
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/run-script.md
---

## 说明

在工作流中调用已注册的应用程序操作。可用于触发非数据转换的平台工作——即应用公开用于自动化的操作。

## 配置

### 要执行的应用程序操作

要调用的操作。

### 文件路径

适用于接受文件的操作：

- **Document directory**——要传入的文档账户和路径。
- **File parameter name**——操作期望路径所使用的参数名。默认为 `document_path`；仅当操作使用了不同的名称时才需更改。

### 可选参数

与文件路径一起传给操作的名称/值对。

## 相关内容

- [常规步骤](/zh-cn/reference/workflow-steps/general/)
- [User Defined Transform](/zh-cn/reference/workflow-steps/general/user-defined-transform/)
- [Run Remote Python](/zh-cn/reference/workflow-steps/general/run-remote-python/)
