---
title: TO_DAYS (Lakehouse v1)
description: TO_DAYS — converte um número especificado de dias em um tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-days.md
---

Converte um número especificado de dias em um tipo Interval.

- Aceita inteiros positivos, zero e inteiros negativos como entrada.

## Sintaxe do Analyze

```python
func.to_days(<days>)
```

## Exemplos do Analyze

```python
func.to_days(2)
┌──────────────────────────────────────────────────────┐
│ func.to_days(2)                                      │
├──────────────────────────────────────────────────────┤
│ 200 days                                             │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_DAYS(<days>)
```

## Tipo de retorno

Interval (representado em dias).

## Exemplos de SQL

```sql
SELECT TO_DAYS(2), TO_DAYS(0), TO_DAYS(-2);

┌────────────────────────────────────────┐
│ to_days(2) │ to_days(0) │ to_days(- 2) │
├────────────┼────────────┼──────────────┤
│ 2 days     │ 00:00:00   │ -2 days      │
└────────────────────────────────────────┘
```
