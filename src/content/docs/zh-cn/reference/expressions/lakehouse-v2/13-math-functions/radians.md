---
title: RADIANS (Lakehouse v2)
description: RADIANS — 将角度转换为弧度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/radians.md
---

将角度转换为弧度。

## Analyze 语法

```python
func.radians(<x>)
```

## Analyze 示例

```python
func.radians(180)

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```

## SQL 语法

```sql
RADIANS(<x>)
```

## SQL 示例

```sql
SELECT RADIANS(180);

┌───────────────────┐
│ 3.141592653589793  │
└───────────────────┘
```
