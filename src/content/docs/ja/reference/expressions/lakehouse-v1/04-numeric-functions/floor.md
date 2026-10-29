---
title: FLOOR（Lakehouse v1）
description: FLOOR — 数値を切り捨てます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/floor.md
---

数値を切り捨てます。

## Analyze 構文

```python
func.floor( <x> )
```

## Analyze の例

```python
func.floor(1.23)

┌──────────────────┐
│ func.floor(1.23) │
├──────────────────┤
│                1 │
└──────────────────┘
```

## SQL 構文

```sql
FLOOR( <x> )
```

## SQL の例

```sql
SELECT FLOOR(1.23);

┌─────────────┐
│ floor(1.23) │
├─────────────┤
│           1 │
└─────────────┘
```
