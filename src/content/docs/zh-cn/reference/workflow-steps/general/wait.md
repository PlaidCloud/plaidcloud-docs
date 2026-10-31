---
title: 等待
description: 在 PlaidCloud 工作流步骤中添加定时延迟，在继续执行下一步之前暂停指定的时长。
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/wait.md
---

## 说明


等待转换用于将处理暂停指定的时长。在等待其他系统的 I/O 操作，或在开发期间调试工作流时尤其有用。



## 持续时间参数


使用**持续时间**微调框指定一个非负整数值。



接下来，从下拉菜单中指定时间单位。可选择以下单位：


* 秒
* 分钟
* 小时

## 等待某个时间或文件

**其他等待**部分包含以下字段。步骤在持续时间之后按此顺序等待它们：

* **毫秒**（`milliseconds`）——在持续时间之外额外等待的毫秒数。
* **直到一天中的时间**（`until_time`）——然后休眠，直到时钟下次读到这个一天中的时间（UTC），格式为 `HH:MM:SS`。
* **等待文件**（`file`）——然后等待这个 Document 文件 `{account, path}` 发生更改。**文件更改**（`file_event`）是要等待的更改：`modified`（默认）、`created` 或 `deleted`。步骤每隔**检查文件的间隔（秒）**（`poll_seconds`，默认 5）查看一次文件，最长等待**文件最长等待时间（秒）**（`max_wait_seconds`，默认 3600，最长一天），然后带着警告结束，工作流继续运行。等待 `created` 时，如果文件已经存在，等待立即结束；等待 `modified` 或 `deleted` 时，如果文件缺失，则不等待，直接带着指明路径的警告结束。
