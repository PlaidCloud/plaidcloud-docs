---
title: TOMORROW (Lakehouse v1)
description: TOMORROW — devuelve la fecha de mañana, igual que today() + 1.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/tomorrow.md
---

Devuelve la fecha de mañana, igual que `today() + 1`.

## Sintaxis de Analyze

```python
func.tomorrow()
```

## Ejemplos de Analyze

```python
func.tomorrow()
┌─────────────────┐
│ func.tomorrow() │
├─────────────────┤
│ 2021-09-03      │
└─────────────────┘
```

## Sintaxis SQL

```sql
TOMORROW()
```

## Tipo de retorno

`DATE`, devuelve la fecha en formato “YYYY-MM-DD”.

## Ejemplos de SQL

```sql
SELECT TOMORROW();
┌────────────┐
│ TOMORROW() │
├────────────┤
│ 2021-09-04 │
└────────────┘

SELECT TODAY()+1;
┌───────────────┐
│ (TODAY() + 1) │
├───────────────┤
│ 2021-09-04    │
└───────────────┘
```
