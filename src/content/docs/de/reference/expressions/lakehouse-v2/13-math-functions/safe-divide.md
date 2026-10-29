---
title: SAFE_DIVIDE (Lakehouse v2)
description: SAFE_DIVIDE – eine PlaidCloud-Funktion, die zwei Zahlen dividiert und bei einem Nenner von null einen Wert Ihrer Wahl zurückgibt, statt einen Fehler auszulösen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/safe-divide.md
---

Eine PlaidCloud-Funktion, die auf jeder Lakehouse-Engine verfügbar ist. Dividiert die erste Zahl durch die zweite. Ist der Nenner null oder eine der beiden Seiten NULL, ist das Ergebnis NULL, sofern kein dritter Wert angegeben wird. In diesem Fall wird stattdessen dieser Wert zurückgegeben. Beide Seiten werden zuvor in `DECIMAL(38, 10)` umgewandelt, sodass Ganzzahlspalten ohne Abschneiden dividiert werden.

## Analyze-Syntax

```python
func.safe_divide(<numerator>, <denominator>, <divide_by_zero_value>)

func.safe_divide(<numerator>, <denominator>)
```

## Analyze-Beispiele

```python
func.safe_divide(table.revenue, table.units, 0)

| revenue | units | safe_divide |
|---------|-------|-------------|
| 100     | 8     | 12.5        |
| 100     | 0     | 0           |
| 100     | NULL  | 0           |
```

```python
func.safe_divide(table.revenue, table.units, None)

| revenue | units | safe_divide |
|---------|-------|-------------|
| 100     | 8     | 12.5        |
| 100     | 0     | NULL        |
```

## SQL-Äquivalent

Es gibt keine SQL-Funktion mit diesem Namen. Der Ausdruck wird wie folgt kompiliert:

```sql
COALESCE(CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0), <divide_by_zero_value>)
```

Ohne das dritte Argument entfällt COALESCE, und ein Nenner von null ergibt NULL:

```sql
CAST(<numerator> AS DECIMAL(38, 10)) / NULLIF(CAST(<denominator> AS DECIMAL(38, 10)), 0)
```
