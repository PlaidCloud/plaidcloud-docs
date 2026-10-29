---
title: TO_YEARS (Lakehouse v1)
description: TO_YEARS — converte um número especificado de anos em um tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-years.md
---

Converte um número especificado de anos em um tipo Interval.

- Aceita inteiros positivos, zero e inteiros negativos como entrada.

## Sintaxe do Analyze

```python
func.to_years(<years>)
```

## Exemplos do Analyze

```python
func.to_years(2)
┌──────────────────────────────────────────────────────┐
│ func.to_years(2)                                     │
├──────────────────────────────────────────────────────┤
│ 2 years                                              │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_YEARS(<years>)
```

## Tipo de retorno

Interval (representado em anos).

## Exemplos de SQL

```sql
SELECT TO_YEARS(2), TO_YEARS(0), TO_YEARS((- 2));

┌───────────────────────────────────────────┐
│ to_years(2) │ to_years(0) │ to_years(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 2 years     │ 00:00:00    │ -2 years      │
└───────────────────────────────────────────┘
```
