---
title: TO_WEEKS (Lakehouse v1)
description: TO_WEEKS — converte um número especificado de semanas num tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-weeks.md
---

Converte um número especificado de semanas num tipo Interval.

- Aceita números inteiros positivos, zero e números inteiros negativos como entrada.

## Sintaxe do Analyze

```python
func.to_weeks(<weeks>)
```

## Exemplos do Analyze

```python
func.to_weeks(2)
┌──────────────────────────────────────────────────────┐
│ func.to_weeks(2)                                     │
├──────────────────────────────────────────────────────┤
│ 14 days                                              │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_WEEKS(<weeks>)
```

## Tipo de Retorno

Interval (representado em dias).

## Exemplos SQL

```sql
SELECT TO_WEEKS(2), TO_WEEKS(0), TO_WEEKS((- 2));

┌───────────────────────────────────────────┐
│ to_weeks(2) │ to_weeks(0) │ to_weeks(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 14 days     │ 00:00:00    │ -14 days      │
└───────────────────────────────────────────┘
```
