---
title: DSQRT (Lakehouse v2)
description: DSQRT — `SQRT` 的别名。参见 [SQRT](../sqrt/)。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dsqrt.md
---

`SQRT` 的别名。参见 [SQRT](../sqrt/)。

## Analyze 语法

```python
func.dsqrt(144)
```

## Analyze 示例

```python
func.dsqrt(144)

┌──────┐
│ 12.0 │
└──────┘
```

## SQL 语法

```sql
DSQRT(<x>)
```

## SQL 示例

```sql
SELECT DSQRT(144);

┌──────┐
│ 12.0 │
└──────┘
```
