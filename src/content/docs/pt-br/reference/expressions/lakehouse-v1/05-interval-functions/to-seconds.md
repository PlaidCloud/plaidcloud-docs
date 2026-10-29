---
title: TO_SECONDS (Lakehouse v1)
description: TO_SECONDS — converte um número especificado de segundos em um tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-seconds.md
---

Converte um número especificado de segundos em um tipo Interval.

- Aceita inteiros positivos, zero e inteiros negativos como entrada.

## Sintaxe do Analyze

```python
func.to_seconds(<seconds>)
```

## Exemplos do Analyze

```python
func.to_seconds(2)
┌──────────────────────────────────────────────────────┐
│ func.to_seconds(2)                                   │
├──────────────────────────────────────────────────────┤
│ 0:00:02                                              │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_SECONDS(<seconds>)
```

## Aliases

- [EPOCH](../epoch)

## Tipo de retorno

Interval (no formato `hh:mm:ss`).

## Exemplos de SQL

```sql
SELECT TO_SECONDS(2), TO_SECONDS(0), TO_SECONDS((- 2));

┌─────────────────────────────────────────────────┐
│ to_seconds(2) │ to_seconds(0) │ to_seconds(- 2) │
├───────────────┼───────────────┼─────────────────┤
│ 0:00:02       │ 00:00:00      │ -0:00:02        │
└─────────────────────────────────────────────────┘
```
