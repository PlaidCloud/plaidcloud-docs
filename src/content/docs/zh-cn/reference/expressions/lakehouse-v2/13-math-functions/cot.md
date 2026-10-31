---
title: COT (Lakehouse v2)
description: COT — 返回数值的余切值（弧度）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cot.md
---

返回数值的余切值（弧度）。

## Analyze 语法

```python
func.cot(<x>)
```

## Analyze 示例

```python
func.cot(1)

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```

## SQL 语法

```sql
COT(<x>)
```

## SQL 示例

```sql
SELECT COT(1);

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```
