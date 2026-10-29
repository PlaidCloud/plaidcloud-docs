---
title: TO_DECADES (Lakehouse v1)
description: TO_DECADES — converte um número especificado de décadas num tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-decades.md
---

Converte um número especificado de décadas num tipo Interval.

- Aceita números inteiros positivos, zero e números inteiros negativos como entrada.

## Sintaxe do Analyze

```python
func.to_decades(<decades>)
```

## Exemplos do Analyze

```python
func.to_decades(2)
┌──────────────────────────────────────────────────────┐
│ func.to_decades(2)                                   │
├──────────────────────────────────────────────────────┤
│ 20 years                                             │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_DECADES(<decades>)
```

## Tipo de Retorno

Interval (representado em anos).

## Exemplos SQL

```sql
SELECT TO_DECADES(2), TO_DECADES(0), TO_DECADES((- 2));

┌─────────────────────────────────────────────────┐
│ to_decades(2) │ to_decades(0) │ to_decades(- 2) │
├───────────────┼───────────────┼─────────────────┤
│ 20 years      │ 00:00:00      │ -20 years       │
└─────────────────────────────────────────────────┘
```
