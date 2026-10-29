---
title: COSH (Lakehouse v2)
description: COSH — 返回数值的双曲余弦值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cosh.md
---

返回数值的双曲余弦值。

## Analyze 语法

```python
func.cosh(<x>)
```

## Analyze 示例

```python
func.cosh(0)

┌─────┐
│ 1.0  │
└─────┘
```

## SQL 语法

```sql
COSH(<x>)
```

## SQL 示例

```sql
SELECT COSH(0);

┌─────┐
│ 1.0  │
└─────┘
```
