---
title: TO_MILLENNIA (Lakehouse v1)
description: TO_MILLENNIA — converte um número especificado de milênios em um tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-millennia.md
---

Converte um número especificado de milênios em um tipo Interval.

- Aceita inteiros positivos, zero e inteiros negativos como entrada.

## Sintaxe do Analyze

```python
func.to_millennia(<millennia>)
```

## Exemplos do Analyze

```python
func.to_millennia(2)
┌──────────────────────────────────────────────────────┐
│ func.to_millennia(2)                                 │
├──────────────────────────────────────────────────────┤
│ 2000 years                                            │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_MILLENNIA(<millennia>)
```

## Tipo de retorno

Interval (representado em anos).

## Exemplos de SQL

```sql
SELECT TO_MILLENNIA(2), TO_MILLENNIA(0), TO_MILLENNIA((- 2));

┌───────────────────────────────────────────────────────┐
│ to_millennia(2) │ to_millennia(0) │ to_millennia(- 2) │
├─────────────────┼─────────────────┼───────────────────┤
│ 2000 years      │ 00:00:00        │ -2000 years       │
└───────────────────────────────────────────────────────┘
```
