---
title: ATAN2 (Lakehouse v1)
description: ATAN2 – gibt den Arkustangens der beiden Variablen x und y zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/atan2.md
---

Gibt den Arkustangens der beiden Variablen `x` und `y` zurück. Das Ergebnis entspricht der Berechnung des Arkustangens von `y` / `x`, wobei jedoch die Vorzeichen beider Argumente den Quadranten des Ergebnisses bestimmen. `ATAN(y, x)` ist ein Synonym für `ATAN2(y, x)`.

## Analyze-Syntax

```python
func.atan2( <y, x> )
```

## Analyze-Beispiele

```python
func.atan2((- 2), 2)

┌─────────────────────┐
│ func.atan2((- 2), 2)│
├─────────────────────┤
│ -0.7853981633974483 │
└─────────────────────┘
```

## SQL-Syntax

```sql
ATAN2( <y, x> )
```

## SQL-Beispiele

```sql
SELECT ATAN2(-2, 2);

┌─────────────────────┐
│   atan2((- 2), 2)   │
├─────────────────────┤
│ -0.7853981633974483 │
└─────────────────────┘
```
