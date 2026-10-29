---
title: TODAY (Lakehouse v1)
description: TODAY — devuelve la fecha actual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/today.md
---

Devuelve la fecha actual.

## Sintaxis de Analyze

```python
func.today()
```

## Ejemplos de Analyze

```python
func.today()
┌──────────────┐
│ func.today() │
├──────────────┤
│ 2021-09-03   │
└──────────────┘
```

## Sintaxis SQL

```sql
TODAY()
```

## Tipo de retorno

`DATE`, devuelve la fecha en formato “YYYY-MM-DD”.

## Ejemplos de SQL

```sql
SELECT TODAY();
┌────────────┐
│ TODAY()    │
├────────────┤
│ 2021-09-03 │
└────────────┘
```
