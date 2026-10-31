---
title: DEGREES (Lakehouse v2)
description: DEGREES — 将弧度转换为角度。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/degrees.md
---

将弧度转换为角度。

## Analyze 语法

```python
func.degrees(<x>)
```

## Analyze 示例

```python
func.degrees(3.141592653589793)

┌───────┐
│ 180.0  │
└───────┘
```

## SQL 语法

```sql
DEGREES(<x>)
```

## SQL 示例

```sql
SELECT DEGREES(PI());

┌───────┐
│ 180.0  │
└───────┘
```
