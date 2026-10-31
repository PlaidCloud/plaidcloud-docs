---
title: LEAST (Lakehouse v1)
description: LEAST – gibt den kleinsten Wert aus einer Menge von Werten zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/least.md
---

Gibt den kleinsten Wert aus einer Menge von Werten zurück.

## Analyze-Syntax

```python
func.least((<value1>, <value2> ...))
```

## Analyze-Beispiele

```python
func.least((5, 9, 4))

┌───────────────────────┐
│ func.least((5, 9, 4)) │
├───────────────────────┤
│                     4 │
└───────────────────────┘
```

## SQL-Syntax

```sql
LEAST(<value1>, <value2> ...)
```

## SQL-Beispiele

```sql
SELECT LEAST(5, 9, 4);

┌────────────────┐
│ least(5, 9, 4) │
├────────────────┤
│              4 │
└────────────────┘
```
