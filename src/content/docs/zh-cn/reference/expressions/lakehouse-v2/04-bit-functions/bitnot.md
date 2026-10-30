---
title: BITNOT (Lakehouse v2)
description: BITNOT：返回数值的按位取反结果。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitnot.md
---

返回数值的按位取反结果。

## Analyze 语法

```python
func.bitnot(<x>)
```

## Analyze 示例

```python
func.bitnot(0)

┌──────┐
│ '-1'  │
└──────┘
```

## SQL 语法

```sql
BITNOT(<x>)
```

## SQL 示例

```sql
SELECT BITNOT(0);

┌────┐
│ -1  │
└────┘
```
