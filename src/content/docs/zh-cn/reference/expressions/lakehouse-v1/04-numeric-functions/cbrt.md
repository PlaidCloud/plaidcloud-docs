---
title: CBRT（Lakehouse v1）
description: CBRT——返回非负数 x 的立方根。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/cbrt.md
---

返回非负数 `x` 的立方根。

## Analyze 语法

```python
func.cbrt( <x> )
```

## Analyze 示例

```python
func.cbrt(27)

┌───────────────┐
│ func.cbrt(27) │
├───────────────┤
│             3 │
└───────────────┘
```

## SQL 语法

```sql
CBRT( <x> )
```

## SQL 示例

```sql
SELECT CBRT(27);

┌──────────┐
│ cbrt(27) │
├──────────┤
│        3 │
└──────────┘
```
