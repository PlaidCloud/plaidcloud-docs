---
title: COS (Lakehouse v2)
description: COS — 返回数值的余弦值（弧度）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cos.md
---

返回数值的余弦值（弧度）。

## Analyze 语法

```python
func.cos(<x>)
```

## Analyze 示例

```python
func.cos(0)

┌─────┐
│ 1.0  │
└─────┘
```

## SQL 语法

```sql
COS(<x>)
```

## SQL 示例

```sql
SELECT COS(0);

┌─────┐
│ 1.0  │
└─────┘
```
