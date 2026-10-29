---
title: DLOG1 (Lakehouse v2)
description: DLOG1 — `LN` 的别名。参见 [LN](../ln/)。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dlog1.md
---

`LN` 的别名。参见 [LN](../ln/)。

## Analyze 语法

```python
func.dlog1(2.718281828459045)
```

## Analyze 示例

```python
func.dlog1(2.718281828459045)

┌─────┐
│ 1.0 │
└─────┘
```

## SQL 语法

```sql
DLOG1(<x>)
```

## SQL 示例

```sql
SELECT DLOG1(2.718281828459045);

┌─────┐
│ 1.0 │
└─────┘
```
