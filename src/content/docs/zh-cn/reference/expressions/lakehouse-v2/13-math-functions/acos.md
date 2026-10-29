---
title: ACOS (Lakehouse v2)
description: ACOS — 返回数值的反余弦值（弧度）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/acos.md
---

返回数值的反余弦值（弧度）。

## Analyze 语法

```python
func.acos(<x>)
```

## Analyze 示例

```python
func.acos(0.5)

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```

## SQL 语法

```sql
ACOS(<x>)
```

## SQL 示例

```sql
SELECT ACOS(0.5);

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```
