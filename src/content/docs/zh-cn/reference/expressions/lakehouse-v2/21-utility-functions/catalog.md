---
title: CATALOG (Lakehouse v2)
description: CATALOG：返回当前目录的名称。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/catalog.md
---

返回当前目录的名称。

## Analyze 语法

```python
func.catalog()
```

## Analyze 示例

```python
func.catalog()

┌───────────────────┐
│ 'default_catalog'  │
└───────────────────┘
```

## SQL 语法

```sql
CATALOG()
```

## SQL 示例

```sql
SELECT CATALOG();

┌─────────────────┐
│ default_catalog  │
└─────────────────┘
```
