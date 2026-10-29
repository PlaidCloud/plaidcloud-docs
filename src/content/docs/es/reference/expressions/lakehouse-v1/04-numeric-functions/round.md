---
title: ROUND (Lakehouse v1)
description: ROUND — redondea el argumento x a d posiciones decimales.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/round.md
---

Redondea el argumento x a d posiciones decimales. El algoritmo de redondeo depende del tipo de datos de x. Si no se especifica, d es 0 de forma predeterminada. d puede ser negativo para que d dígitos a la izquierda del separador decimal del valor x se conviertan en cero. El valor absoluto máximo de d es 30; los dígitos que superen 30 (o -30) se truncan.

Al usar el resultado de esta función en cálculos, tenga en cuenta posibles problemas de precisión, ya que su tipo de datos devuelto es DOUBLE, lo que puede afectar a la exactitud final:

```sql
SELECT ROUND(4/7, 4) - ROUND(3/7, 4); -- Result: 0.14280000000000004
SELECT ROUND(4/7, 4)::DECIMAL(8,4) - ROUND(3/7, 4)::DECIMAL(8,4); -- Result: 0.1428
```

## Sintaxis de Analyze

```python
func.round( <x, d> )
```

## Ejemplos de Analyze

```python
func.round(0.123, 2)

┌──────────────────────┐
│ func.round(0.123, 2) │
├──────────────────────┤
│                 0.12 │
└──────────────────────┘
```

## Sintaxis de SQL

```sql
ROUND( <x, d> )
```

## Ejemplos de SQL

```sql
SELECT ROUND(0.123, 2);

┌─────────────────┐
│ round(0.123, 2) │
├─────────────────┤
│ 0.12            │
└─────────────────┘
```
