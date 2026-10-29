---
title: VERSION (Lakehouse v2)
description: VERSION：返回 StarRocks 的 MySQL 协议版本。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/version.md
---

返回 StarRocks 的 MySQL 协议版本。

## Analyze 语法

```python
func.version()
```

## Analyze 示例

```python
func.version()

┌─────────┐
│ '5.1.0'  │
└─────────┘
```

## SQL 语法

```sql
VERSION()
```

## SQL 示例

```sql
SELECT VERSION();

┌───────┐
│ 5.1.0  │
└───────┘
```
