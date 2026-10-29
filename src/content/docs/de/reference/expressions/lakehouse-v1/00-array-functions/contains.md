---
title: CONTAINS (Lakehouse v1)
description: CONTAINS – prüft, ob das Array ein bestimmtes Element enthält.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/contains.md
---

Prüft, ob das Array ein bestimmtes Element enthält.


## Analyze-Syntax

```python
func.contains( <array>, <element> )
```

## Analyze-Beispiele

```python
func.contains([1, 2], 1)

┌───────────────────────────┐
│ func.contains([1, 2], 1)  │
├───────────────────────────┤
│ true                      │
└───────────────────────────┘
```

## SQL-Syntax

```sql
CONTAINS( <array>, <element> )
```

## Aliasse

- [ARRAY_CONTAINS](../array-contains)

## SQL-Beispiele

```sql
SELECT ARRAY_CONTAINS([1, 2], 1), CONTAINS([1, 2], 1);

┌─────────────────────────────────────────────────┐
│ array_contains([1, 2], 1) │ contains([1, 2], 1) │
├───────────────────────────┼─────────────────────┤
│ true                      │ true                │
└─────────────────────────────────────────────────┘
```
