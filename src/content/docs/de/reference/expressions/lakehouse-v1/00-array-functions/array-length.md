---
title: ARRAY_LENGTH (Lakehouse v1)
description: ARRAY_LENGTH – gibt die Länge eines Arrays zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-length.md
---

Gibt die Länge eines Arrays zurück.

## Analyze-Syntax

```python
func.array_length( <array> )
```

## Analyze-Beispiele

```python
func.array_length([1, 2])

┌────────────────────────────┐
│ func.array_length([1, 2])  │
├────────────────────────────┤
│                          2 │
└────────────────────────────┘
```

## SQL-Syntax

```sql
ARRAY_LENGTH( <array> )
```

## SQL-Beispiele

```sql
SELECT ARRAY_LENGTH([1, 2]);

┌──────────────────────┐
│ array_length([1, 2]) │
├──────────────────────┤
│                    2 │
└──────────────────────┘
```
