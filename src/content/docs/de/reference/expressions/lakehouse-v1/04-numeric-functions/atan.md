---
title: ATAN (Lakehouse v1)
description: ATAN – gibt den Arkustangens von x zurück, also den Wert, dessen Tangens x ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/atan.md
---

Gibt den Arkustangens von `x` zurück, also den Wert, dessen Tangens `x` ist.

## Analyze-Syntax

```python
func.atan( <x> )
```

## Analyze-Beispiele

```python
func.atan(-2)

┌─────────────────────┐
│  func.atan((- 2))   │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```

## SQL-Syntax

```sql
ATAN( <x> )
```

## SQL-Beispiele

```sql
SELECT ATAN(-2);

┌─────────────────────┐
│     atan((- 2))     │
├─────────────────────┤
│ -1.1071487177940906 │
└─────────────────────┘
```
