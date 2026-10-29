---
title: DLOG10 (Lakehouse v2)
description: DLOG10 — `LOG10` 的别名。参见 [LOG10](../log10/)。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dlog10.md
---

`LOG10` 的别名。参见 [LOG10](../log10/)。

## Analyze 语法

```python
func.dlog10(1000)
```

## Analyze 示例

```python
func.dlog10(1000)

┌─────┐
│ 3.0 │
└─────┘
```

## SQL 语法

```sql
DLOG10(<x>)
```

## SQL 示例

```sql
SELECT DLOG10(1000);

┌─────┐
│ 3.0 │
└─────┘
```
