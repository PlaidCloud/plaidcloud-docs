---
title: LN（Lakehouse v1）
description: LN——返回 x 的自然对数，即以 e 为底的 x 的对数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/ln.md
---

返回 `x` 的自然对数，即以 e 为底的 `x` 的对数。如果 x 小于或等于 0.0E0，则函数返回 NULL。

## Analyze 语法

```python
func.ln( <x> )
```

## Analyze 示例

```python
func.ln(2)

┌────────────────────┐
│     func.ln(2)     │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```

## SQL 语法

```sql
LN( <x> )
```

## SQL 示例

```sql
SELECT LN(2);

┌────────────────────┐
│        ln(2)       │
├────────────────────┤
│ 0.6931471805599453 │
└────────────────────┘
```
