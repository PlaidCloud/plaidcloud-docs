---
title: TO_MILLISECONDS (Lakehouse v1)
description: TO_MILLISECONDS — converte um número especificado de milissegundos em um tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-milliseconds.md
---

Converte um número especificado de milissegundos em um tipo Interval.

- Aceita inteiros positivos, zero e inteiros negativos como entrada.

## Sintaxe do Analyze

```python
func.to_milliseconds(<milliseconds>)
```

## Exemplos do Analyze

```python
func.to_milliseconds(2)
┌──────────────────────────────────────────────────────┐
│ func.to_milliseconds(2)                              │
├──────────────────────────────────────────────────────┤
│  0:00:00.002                                         │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_MILLISECONDS(<milliseconds>)
```

## Tipo de retorno

Interval (no formato `hh:mm:ss.sss`).

## Exemplos de SQL

```sql
SELECT TO_MILLISECONDS(2), TO_MILLISECONDS(0), TO_MILLISECONDS((- 2));

┌────────────────────────────────────────────────────────────────┐
│ to_milliseconds(2) │ to_milliseconds(0) │ to_milliseconds(- 2) │
├────────────────────┼────────────────────┼──────────────────────┤
│ 0:00:00.002        │ 00:00:00           │ -0:00:00.002         │
└────────────────────────────────────────────────────────────────┘
```
