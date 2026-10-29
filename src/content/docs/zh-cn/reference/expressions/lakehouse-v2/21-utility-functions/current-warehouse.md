---
title: CURRENT_WAREHOUSE (Lakehouse v2)
description: CURRENT_WAREHOUSE：返回当前仓库的名称。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-warehouse.md
---

返回当前仓库的名称。

## Analyze 语法

```python
func.current_warehouse()
```

## Analyze 示例

```python
func.current_warehouse()

┌───────────────────┐
│ default_warehouse │
└───────────────────┘
```

## SQL 语法

```sql
CURRENT_WAREHOUSE()
```

## SQL 示例

```sql
SELECT CURRENT_WAREHOUSE();

┌───────────────────┐
│ default_warehouse │
└───────────────────┘
```
