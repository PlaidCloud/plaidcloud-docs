---
title: Lakehouse v2 表达式
description: 基于 StarRocks 4.1 SQL 函数的 Lakehouse v2 表达式，附 SQLAlchemy 参考。
sidebar:
  label: Lakehouse v2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/index.md
---

Lakehouse v2 基于 [StarRocks](https://www.starrocks.io/) 4.1 构建。对于下面的每个函数，本站提供 PlaidCloud 风格的语法和示例；如需包含所有边界情况和参数变体的权威上游参考，请参阅 **[StarRocks SQL 函数参考](https://docs.starrocks.io/docs/sql-reference/sql-functions/)**。

## 聚合函数

- [聚合函数](./01-aggregate-functions) — 计算求和、平均值、计数等汇总值
- [百分位函数](./15-percentile-functions) — 计算百分位值并管理百分位状态

## 标量函数

- [数组函数](./02-array-functions) — 执行数组操作
- [二进制函数](./03-binary-functions) — 在二进制和字符串格式之间转换
- [位函数](./04-bit-functions) — 执行按位运算
- [位图函数](./05-bitmap-functions) — 执行位图操作和处理
- [条件函数](./06-condition-functions) — 实现条件逻辑和 case 语句
- [加密函数](./07-cryptographic-functions) — 加密、解密和哈希数据
- [日期和时间函数](./08-date-time-functions) — 处理和格式化日期与时间
- [字典函数](./09-dictionary-functions) — 在字典表中查找值
- [哈希函数](./10-hash-functions) — 使用 MurmurHash 和 xxHash 生成哈希值
- [JSON 函数](./11-json-functions) — 创建、查询和处理 JSON 数据
- [映射函数](./12-map-functions) — 创建和处理映射数据结构
- [数学函数](./13-math-functions) — 执行计算和数值运算
- [模式匹配函数](./14-pattern-matching-functions) — 使用 LIKE 和正则表达式匹配字符串
- [标量函数（HLL）](./16-scalar-functions) — HyperLogLog 基数估算函数
- [空间函数](./17-spatial-functions) — 处理地理空间数据
- [字符串函数](./18-string-functions) — 处理字符串并执行文本操作
- [结构体函数](./19-struct-functions) — 创建并使用结构体数据类型
- [Variant 函数](./22-variant-functions) — 查询并检查 VARIANT 数据类型

## 表函数

- [表函数](./20-table-functions) — 以表格形式返回结果

## 实用函数和元函数

- [实用函数](./21-utility-functions) — 访问系统信息和会话实用工具
- [元函数](./23-meta-functions) — 检查物化视图、内存和诊断信息

## 管理 Lakehouse

- [Lakehouse 管理](./lakehouse-management/) — 运行查询、浏览目录、管理仓库并监控计算资源
