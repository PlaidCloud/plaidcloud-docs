---
title: TO_BOOLEAN (Lakehouse v1)
description: TO_BOOLEAN – wandelt einen Wert in den Datentyp BOOLEAN um.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-boolean.md
---

Wandelt einen Wert in den Datentyp BOOLEAN um.

## Analyze-Syntax

```python
func.to_boolean( <expr> )
```

## Analyze-Beispiele

```python
func.to_boolean('true')

┌──────────────────────────┐
│ func.to_boolean('true')  │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## SQL-Syntax

```sql
TO_BOOLEAN( <expr> )
```

## SQL-Beispiele

```sql
SELECT TO_BOOLEAN('true');

┌────────────────────┐
│ to_boolean('true') │
├────────────────────┤
│ true               │
└────────────────────┘
```
