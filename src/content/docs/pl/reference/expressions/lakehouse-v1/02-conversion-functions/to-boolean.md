---
title: TO_BOOLEAN (Lakehouse v1)
description: TO_BOOLEAN — konwertuje wartość na typ danych BOOLEAN.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-boolean.md
---

Konwertuje wartość na typ danych BOOLEAN.

## Składnia Analyze

```python
func.to_boolean( <expr> )
```

## Przykłady Analyze

```python
func.to_boolean('true')

┌──────────────────────────┐
│ func.to_boolean('true')  │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## Składnia SQL

```sql
TO_BOOLEAN( <expr> )
```

## Przykłady SQL

```sql
SELECT TO_BOOLEAN('true');

┌────────────────────┐
│ to_boolean('true') │
├────────────────────┤
│ true               │
└────────────────────┘
```
