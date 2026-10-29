---
title: RAND(n) (Lakehouse v1)
description: RAND(n) — devuelve un valor de coma flotante aleatorio v en el rango 0 &lt;= v &lt; 1.0.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/randn.md
---

Devuelve un valor de coma flotante aleatorio v en el rango 0 &lt;= v &lt; 1.0. Para obtener un entero aleatorio R en el rango i &lt;= R &lt; j, use la expresión FLOOR(i + RAND() * (j − i)). El argumento `n` se usa como valor semilla. Para valores de argumento iguales, RAND(n) devuelve el mismo valor cada vez y, por tanto, produce una secuencia repetible de valores de columna.

## Sintaxis de Analyze

```python
func.rand( <n>)
```

## Ejemplos de Analyze

```python
func.rand(1)

┌────────────────────┐
│    func.rand(1)    │
├────────────────────┤
│ 0.7133693869548766 │
└────────────────────┘
```

## Sintaxis de SQL

```sql
RAND( <n>)
```

## Ejemplos de SQL

```sql
SELECT RAND(1);

┌────────────────────┐
│       rand(1)      │
├────────────────────┤
│ 0.7133693869548766 │
└────────────────────┘
```
