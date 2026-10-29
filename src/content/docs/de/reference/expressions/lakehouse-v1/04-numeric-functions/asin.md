---
title: ASIN (Lakehouse v1)
description: ASIN – gibt den Arkussinus von x zurück, also den Wert, dessen Sinus x ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/asin.md
---

Gibt den Arkussinus von `x` zurück, also den Wert, dessen Sinus `x` ist. Gibt NULL zurück, wenn `x` nicht im Bereich von -1 bis 1 liegt.

## Analyze-Syntax

```python
func.asin( <x> )
```

## Analyze-Beispiele

```python
func.asin(0.2)

┌────────────────────┐
│   func.asin(0.2)   │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```

## SQL-Syntax

```sql
ASIN( <x> )
```

## SQL-Beispiele

```sql
SELECT ASIN(0.2);

┌────────────────────┐
│      asin(0.2)     │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```
