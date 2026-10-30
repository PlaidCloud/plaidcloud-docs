---
title: "[ NOT ] IN (Lakehouse v1)"
description: "[ NOT ] IN – TRUE, wenn ein Wert einem Element einer expliziten Liste entspricht (oder nicht entspricht)."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/in.md
---

Prüft, ob ein Wert in einer expliziten Liste enthalten ist (oder nicht).

## Analyze-Syntax

```python
table.columns.in_((<value1>, <value2> ...))
```

## Analyze-Beispiele

```python
table.columns.in_((<value1>, <value2> ...))

┌──────────────────────────┐
│ table.column.in_((2, 3)) │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## SQL-Syntax

```sql
<value> [ NOT ] IN (<value1>, <value2> ...)
```

## SQL-Beispiele

```sql
SELECT 1 NOT IN (2, 3);

┌────────────────┐
│ 1 not in(2, 3) │
├────────────────┤
│ true           │
└────────────────┘
```
