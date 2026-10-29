---
title: ASIN (Lakehouse v1)
description: ASIN — devuelve el arcoseno de x, es decir, el valor cuyo seno es x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/asin.md
---

Devuelve el arcoseno de `x`, es decir, el valor cuyo seno es `x`. Devuelve NULL si `x` no está en el rango de -1 a 1.

## Sintaxis de Analyze

```python
func.asin( <x> )
```

## Ejemplos de Analyze

```python
func.asin(0.2)

┌────────────────────┐
│   func.asin(0.2)   │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```

## Sintaxis de SQL

```sql
ASIN( <x> )
```

## Ejemplos de SQL

```sql
SELECT ASIN(0.2);

┌────────────────────┐
│      asin(0.2)     │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```
