---
title: TO_CENTURIES (Lakehouse v1)
description: TO_CENTURIES — converte um número especificado de séculos num tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-centuries.md
---

Converte um número especificado de séculos num tipo Interval.

- Aceita números inteiros positivos, zero e números inteiros negativos como entrada.

## Sintaxe do Analyze

```python
func.to_centuries(<centuries>)
```

## Exemplos do Analyze

```python
func.to_centuries(2)
┌──────────────────────────────────────────────────────┐
│ func.to_centuries(2)                                 │
├──────────────────────────────────────────────────────┤
│ 200 years                                            │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_CENTURIES(<centuries>)
```

## Tipo de Retorno

Interval (representado em anos).

## Exemplos SQL

```sql
SELECT TO_CENTURIES(2), TO_CENTURIES(0), TO_CENTURIES(-2);

┌───────────────────────────────────────────────────────┐
│ to_centuries(2) │ to_centuries(0) │ to_centuries(- 2) │
├─────────────────┼─────────────────┼───────────────────┤
│ 200 years       │ 00:00:00        │ -200 years        │
└───────────────────────────────────────────────────────┘
```
