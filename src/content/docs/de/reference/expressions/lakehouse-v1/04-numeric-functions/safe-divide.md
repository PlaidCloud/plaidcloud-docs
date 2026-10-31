---
title: SAFE_DIVIDE (Lakehouse v1)
description: SAFE_DIVIDE – eine PlaidCloud-Funktion, die zwei Zahlen dividiert und bei einem Nenner von null einen frei wählbaren Wert zurückgibt, statt zu fehlschlagen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/safe-divide.md
---

Eine PlaidCloud-Funktion, die auf jeder Lakehouse-Engine verfügbar ist. Dividiert die erste Zahl durch die zweite. Ist der Nenner null oder eine der beiden Seiten NULL, ist das Ergebnis der dritte Wert; übergeben Sie `None`, um NULL zu erhalten. In Lakehouse v1 sind alle drei Argumente erforderlich. Beide Seiten werden zunächst in `DECIMAL(38, 10)` umgewandelt, sodass Ganzzahlspalten ohne Abschneiden dividiert werden.

## Analyze-Syntax

```python
func.safe_divide(<numerator>, <denominator>, <divide_by_zero_value>)
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
