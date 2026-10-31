---
title: TO_MINUTES (Lakehouse v1)
description: TO_MINUTES — converte um número especificado de minutos em um tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-minutes.md
---

Converte um número especificado de minutos em um tipo Interval.

- Aceita inteiros positivos, zero e inteiros negativos como entrada.

## Sintaxe do Analyze

```python
func.to_minutes(<minutes>)
```

## Exemplos do Analyze

```python
func.to_minutes(2)
┌──────────────────────────────────────────────────────┐
│ func.to_minutes(2)                                   │
├──────────────────────────────────────────────────────┤
│ 0:02:00                                              │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_MINUTES(<minutes>)
```

## Tipo de retorno

Interval (no formato `hh:mm:ss`).

## Exemplos de SQL

```sql
SELECT TO_MINUTES(2), TO_MINUTES(0), TO_MINUTES((- 2));

┌─────────────────────────────────────────────────┐
│ to_minutes(2) │ to_minutes(0) │ to_minutes(- 2) │
├───────────────┼───────────────┼─────────────────┤
│ 0:02:00       │ 00:00:00      │ -0:02:00        │
└─────────────────────────────────────────────────┘
```
