---
title: CURRENT_VERSION (Lakehouse v2)
description: CURRENT_VERSION：返回 StarRocks 的当前版本。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-version.md
---

返回 StarRocks 的当前版本。

## Analyze 语法

```python
func.current_version()
```

## Analyze 示例

```python
func.current_version()

┌─────────┐
│ '4.1.0'  │
└─────────┘
```

## SQL 语法

```sql
CURRENT_VERSION()
```

## SQL 示例

```sql
SELECT CURRENT_VERSION();

┌──────────────┐
│ 4.1.0-xxxxxx  │
└──────────────┘
```
