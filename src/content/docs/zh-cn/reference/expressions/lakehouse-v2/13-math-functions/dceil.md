---
title: DCEIL (Lakehouse v2)
description: DCEIL — `CEIL` 的别名。参见 [CEIL](../ceil/)。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dceil.md
---

`CEIL` 的别名。参见 [CEIL](../ceil/)。

## Analyze 语法

```python
func.dceil(3.2)
```

## Analyze 示例

```python
func.dceil(3.2)

┌───┐
│ 4 │
└───┘
```

## SQL 语法

```sql
DCEIL(<x>)
```

## SQL 示例

```sql
SELECT DCEIL(3.2);

┌───┐
│ 4 │
└───┘
```
