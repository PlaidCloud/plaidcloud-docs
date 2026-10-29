---
title: ASIN (Lakehouse v2)
description: ASIN — 返回数值的反正弦值（弧度）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/asin.md
---

返回数值的反正弦值（弧度）。

## Analyze 语法

```python
func.asin(<x>)
```

## Analyze 示例

```python
func.asin(0.5)

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```

## SQL 语法

```sql
ASIN(<x>)
```

## SQL 示例

```sql
SELECT ASIN(0.5);

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```
