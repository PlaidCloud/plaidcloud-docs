---
title: DFLOOR (Lakehouse v2)
description: DFLOOR — `FLOOR` 的别名。参见 [FLOOR](../floor/)。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dfloor.md
---

`FLOOR` 的别名。参见 [FLOOR](../floor/)。

## Analyze 语法

```python
func.dfloor(3.7)
```

## Analyze 示例

```python
func.dfloor(3.7)

┌───┐
│ 3 │
└───┘
```

## SQL 语法

```sql
DFLOOR(<x>)
```

## SQL 示例

```sql
SELECT DFLOOR(3.7);

┌───┐
│ 3 │
└───┘
```
