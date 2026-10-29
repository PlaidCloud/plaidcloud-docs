---
title: CBRT (Lakehouse v2)
description: CBRT — 返回数值的立方根。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cbrt.md
---

返回数值的立方根。

## Analyze 语法

```python
func.cbrt(<x>)
```

## Analyze 示例

```python
func.cbrt(27)

┌─────┐
│ 3.0  │
└─────┘
```

## SQL 语法

```sql
CBRT(<x>)
```

## SQL 示例

```sql
SELECT CBRT(27);

┌─────┐
│ 3.0  │
└─────┘
```
