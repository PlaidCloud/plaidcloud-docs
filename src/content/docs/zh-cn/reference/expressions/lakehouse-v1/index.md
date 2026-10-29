---
title: Lakehouse v1 表达式
description: 基于 Databend SQL 函数的 Lakehouse v1 表达式，并提供使用 func. 前缀的 SQLAlchemy 引用。
sidebar:
  label: Lakehouse v1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/index.md
---

Lakehouse v1 基于 [Databend](https://databend.com/) SQL 引擎构建。对于下列每个函数，本站提供 PlaidCloud 风格的语法和示例；如需包含所有边缘情况和参数变体的权威上游参考，请参阅 **[Databend SQL 函数参考](https://docs.databend.com/sql/sql-functions/)**。

## 标量函数

- [数组函数](./00-array-functions) — 执行数组操作
- [按位表达式函数](./01-bitmap-functions) — 执行按位运算和操作
- [条件表达式函数](./03-conditional-functions) — 实现条件逻辑和 case 语句
- [上下文函数](./15-context-functions) — 提供有关当前 SQL 执行上下文的信息
- [转换函数](./02-conversion-functions) — 转换数据类型和强制转换值
- [日期和时间函数](./05-datetime-functions) — 处理日期和时间并设置其格式
- [地理空间函数](./09-geo-functions) — 处理和操作地理空间数据
- [几何函数](./09-geometry-functions) — 处理和操作地理空间几何数据
- [时间间隔函数](./05-interval-functions) — 创建和操作时间间隔
- [映射函数](./10-map-functions) — 创建和操作映射数据结构
- [数值函数](./04-numeric-functions) — 执行计算和数值运算
- [搜索函数](./10-search-functions) — 使用表达式查找值
- [半结构化和结构化数据函数](./10-semi-structured-functions) — 处理 JSON 和其他结构化数据格式
- [字符串函数](./06-string-functions) — 处理字符串并执行正则表达式操作

## 聚合函数

- [聚合函数](./07-aggregate-functions) — 计算求和、平均值、计数等汇总值
- [窗口函数](./08-window-functions) — 对指定范围的行提供聚合计算

## AI 函数

- [AI 函数](./11-ai-functions) — 利用 AI 和机器学习能力

## 专用函数

- [哈希函数](./12-hash-functions) — 生成用于数据安全和比较的哈希值
- [IP 地址函数](./14-ip-address-functions) — 处理和分析 IP 地址数据
- [UUID 函数](./13-uuid-functions) — 生成和处理 UUID

## 系统函数和表函数

- [序列函数](./18-sequence-functions) — 生成序列值
- [系统函数](./16-system-functions) — 访问系统级信息并执行控制操作
- [表函数](./17-table-functions) — 以表格形式返回结果

## 其他函数

- [字典函数](./19-dictionary-functions) — 处理字典数据结构
- [其他杂项函数](./20-other-functions) — 各种其他函数的集合
- [测试函数](./19-test-functions) — 用于测试目的的函数
