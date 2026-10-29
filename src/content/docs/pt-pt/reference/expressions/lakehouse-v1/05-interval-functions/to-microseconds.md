---
title: TO_MICROSECONDS (Lakehouse v1)
description: TO_MICROSECONDS — converte um número especificado de microssegundos num tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-microseconds.md
---

Converte um número especificado de microssegundos num tipo Interval.

- Aceita números inteiros positivos, zero e números inteiros negativos como entrada.

## Sintaxe do Analyze

```python
func.to_microseconds(<microseconds>)
```

## Exemplos do Analyze

```python
func.to_microseconds(2)
┌──────────────────────────────────────────────────────┐
│ func.to_microseconds(2)                              │
├──────────────────────────────────────────────────────┤
│ 0:00:00.000002                                       │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_MICROSECONDS(<microseconds>)
```

## Tipo de Retorno

Interval (no formato `hh:mm:ss.sssssss`).

## Exemplos SQL

```sql
SELECT TO_MICROSECONDS(2), TO_MICROSECONDS(0), TO_MICROSECONDS((- 2));

┌────────────────────────────────────────────────────────────────┐
│ to_microseconds(2) │ to_microseconds(0) │ to_microseconds(- 2) │
├────────────────────┼────────────────────┼──────────────────────┤
│ 0:00:00.000002     │ 00:00:00           │ -0:00:00.000002      │
└────────────────────────────────────────────────────────────────┘
```
