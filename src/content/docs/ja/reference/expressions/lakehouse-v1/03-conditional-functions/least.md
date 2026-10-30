---
title: LEAST（Lakehouse v1）
description: LEAST — 値の集合から最小値を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/least.md
---

値の集合から最小値を返します。

## Analyze 構文

```python
func.least((<value1>, <value2> ...))
```

## Analyze の例

```python
func.least((5, 9, 4))

┌───────────────────────┐
│ func.least((5, 9, 4)) │
├───────────────────────┤
│                     4 │
└───────────────────────┘
```

## SQL 構文

```sql
LEAST(<value1>, <value2> ...)
```

## SQL の例

```sql
SELECT LEAST(5, 9, 4);

┌────────────────┐
│ least(5, 9, 4) │
├────────────────┤
│              4 │
└────────────────┘
```
