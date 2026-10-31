---
title: NULLIF (Lakehouse v1)
description: NULLIF — devuelve NULL si dos expresiones son iguales.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/nullif.md
---

Devuelve NULL si dos expresiones son iguales. De lo contrario, devuelve expr1. Ambas deben tener el mismo tipo de datos.

## Sintaxis de Analyze

```python
func.nullif(<expr1>, <expr2>)
```

## Ejemplos de Analyze

```python
func.nullif(0, null) 

┌──────────────────────┐
│ func.nullif(0, null) │
├──────────────────────┤
│                    0 │
└──────────────────────┘
```

## Sintaxis de SQL

```sql
NULLIF(<expr1>, <expr2>)
```

## Ejemplos de SQL

```sql
SELECT NULLIF(0, NULL);

┌─────────────────┐
│ nullif(0, null) │
├─────────────────┤
│               0 │
└─────────────────┘
```
