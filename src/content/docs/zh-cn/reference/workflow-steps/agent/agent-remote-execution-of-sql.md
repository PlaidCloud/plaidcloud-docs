---
title: Agent Remote Execution of SQL 步骤
description: 在 PlaidCloud 工作流中通过 PlaidLink 代理远程执行 SQL 查询，在防火墙之后安全地执行数据库操作。
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/agent/agent-remote-execution-of-sql.md
---

## 说明

在 PlaidCloud 只能通过 PlaidLink 代理访问的数据库上执行 SQL，通常是因为数据库位于防火墙之后、专用网络中或本地数据中心内。代理在本地运行 SQL，并将成功或失败的结果报告回 PlaidCloud。

可用于在 PlaidCloud 工作流中触发远程存储过程、刷新例程或维护作业，而无需将源数据库暴露在公共互联网上。

## 对每行运行一次语句

**远程执行：SQL** 步骤直接连接数据库而不是通过代理，它可以对表的每一行运行一次语句，例如为每个输入行调用一个存储过程。将**运行 SQL**设置为**每行一次**，选择一个**驱动因素表**，并填写**参数**。将语句中的每个值写成 `:name` 占位符，例如 `CALL load_region(:region, :period)`，然后在**参数**中把每个占位符映射到提供它的**驱动列**。每个值都会作为绑定参数发送给数据库，绝不会被拼接进语句文本。

每个参数都需要名称和驱动列，且同一个参数不能列出两次。当语句中的某个 `:name` 没有映射，或某个映射不在语句中时，表单会发出警告。驱动因素表必须是表，而不是视图。没有任何行的驱动因素表会带着警告结束且不运行任何内容；超过 100,000 行的驱动因素表会使步骤失败，且一行都不会运行，因此请先对其进行筛选。

## 在一个事务中运行脚本

在**远程执行：SQL** 步骤中，选中**在一个事务中将 SQL 作为语句脚本运行：全部生效或全部不生效**（`transaction`），即可把 SQL 作为语句脚本在单个事务中依次运行，因此要么每条语句都生效，要么全都不生效。
