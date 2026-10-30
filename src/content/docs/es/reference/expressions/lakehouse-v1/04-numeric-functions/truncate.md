---
title: TRUNCATE (Lakehouse v1)
description: TRUNCATE — devuelve el número x truncado a d posiciones decimales.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/truncate.md
---

Devuelve el número `x` truncado a `d` posiciones decimales. Si `d` es 0, el resultado no tiene separador decimal ni parte fraccionaria. `d` puede ser negativo para que `d` dígitos a la izquierda del separador decimal del valor `x` se conviertan en cero. El valor absoluto máximo de `d` es 30; los dígitos que superen 30 (o -30) se truncan.

## Sintaxis de Analyze

```python
func.truncate( <x, d> )
```

## Ejemplos de Analyze

```python
func.truncate(1.223, 1)

┌─────────────────────────┐
│ func.truncate(1.223, 1) │
├─────────────────────────┤
│                     1.2 │
└─────────────────────────┘
```

## Sintaxis de SQL

```sql
TRUNCATE( <x, d> )
```

## Ejemplos de SQL

```sql
SELECT TRUNCATE(1.223, 1);

┌────────────────────┐
│ truncate(1.223, 1) │
├────────────────────┤
│ 1.2                │
└────────────────────┘
```
