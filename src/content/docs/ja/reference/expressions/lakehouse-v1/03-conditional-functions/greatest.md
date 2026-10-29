---
title: GREATEST（Lakehouse v1）
description: GREATEST — 値の集合から最大値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/greatest.md
---

値の集合から最大値を返します。

## Analyze 構文

```python
func.greatest(<value1>, <value2> ...)
```

## Analyze の例

```python
func.greatest((5, 9, 4))

┌──────────────────────────┐
│ func.greatest((5, 9, 4)) │
├──────────────────────────┤
│                        9 │
└──────────────────────────┘
```

## SQL 構文

```sql
GREATEST(<value1>, <value2> ...)
```

## SQL の例

```sql
SELECT GREATEST(5, 9, 4);

┌───────────────────┐
│ greatest(5, 9, 4) │
├───────────────────┤
│                 9 │
└───────────────────┘
```
