---
title: DROUND (Lakehouse v2)
description: DROUND — `ROUND` 的别名。参见 [ROUND](../round/)。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dround.md
---

`ROUND` 的别名。参见 [ROUND](../round/)。

## Analyze 语法

```python
func.dround(3.14159, 2)
```

## Analyze 示例

```python
func.dround(3.14159, 2)

┌──────┐
│ 3.14 │
└──────┘
```

## SQL 语法

```sql
DROUND(<x>)
```

## SQL 示例

```sql
SELECT DROUND(3.14159, 2);

┌──────┐
│ 3.14 │
└──────┘
```
