---
title: RAND() (Lakehouse v1)
description: "RAND() — devuelve un valor de coma flotante aleatorio v en el rango 0 <= v < 1."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/rand.md
---

Devuelve un valor de coma flotante aleatorio v en el rango 0 &lt;= v &lt; 1.0. Para obtener un entero aleatorio R en el rango i &lt;= R &lt; j, use la expresión FLOOR(i + RAND() * (j − i)).

## Sintaxis de Analyze

```python
func.rand()
```

## Ejemplos de Analyze

```python
func.rand()

┌────────────────────┐
│    func.rand()     │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```

## Sintaxis de SQL

```sql
RAND()
```

## Ejemplos de SQL

```sql
SELECT RAND();

┌────────────────────┐
│       rand()       │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```
