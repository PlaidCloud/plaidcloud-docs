---
title: ROUND (Lakehouse v1)
description: ROUND – rundet das Argument x auf d Dezimalstellen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/round.md
---

Rundet das Argument x auf d Dezimalstellen. Der Rundungsalgorithmus hängt vom Datentyp von x ab. Wird d nicht angegeben, ist der Standardwert 0. d kann negativ sein, sodass d Stellen links vom Dezimalpunkt des Werts x zu null werden. Der maximale Absolutwert für d ist 30; darüber hinausgehende Stellen (über 30 bzw. -30) werden abgeschnitten.

Beachten Sie bei der Verwendung des Ergebnisses dieser Funktion in Berechnungen mögliche Genauigkeitsprobleme, da der Rückgabedatentyp DOUBLE ist. Dies kann die endgültige Genauigkeit beeinträchtigen:

```sql
SELECT ROUND(4/7, 4) - ROUND(3/7, 4); -- Result: 0.14280000000000004
SELECT ROUND(4/7, 4)::DECIMAL(8,4) - ROUND(3/7, 4)::DECIMAL(8,4); -- Result: 0.1428
```

## Analyze-Syntax

```python
func.round( <x, d> )
```

## Analyze-Beispiele

```python
func.round(0.123, 2)

┌──────────────────────┐
│ func.round(0.123, 2) │
├──────────────────────┤
│                 0.12 │
└──────────────────────┘
```

## SQL-Syntax

```sql
ROUND( <x, d> )
```

## SQL-Beispiele

```sql
SELECT ROUND(0.123, 2);

┌─────────────────┐
│ round(0.123, 2) │
├─────────────────┤
│ 0.12            │
└─────────────────┘
```
