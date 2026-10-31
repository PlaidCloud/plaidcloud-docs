---
title: ATAN (Lakehouse v2)
description: ATAN — 返回数值的反正切值（弧度）。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/atan.md
---

返回数值的反正切值（弧度）。

## Analyze 语法

```python
func.atan(<x>)
```

## Analyze 示例

```python
func.atan(1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## SQL 语法

```sql
ATAN(<x>)
```

## SQL 示例

```sql
SELECT ATAN(1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```
