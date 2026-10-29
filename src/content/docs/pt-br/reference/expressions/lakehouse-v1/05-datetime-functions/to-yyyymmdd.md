---
title: TO_YYYYMMDD (Lakehouse v1)
description: TO_YYYYMMDD — converte uma data ou data com hora (timestamp/datetime) em um número UInt32.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmdd.md
---

Converte uma data ou data com hora (timestamp/datetime) em um número UInt32 que contém o ano, o mês e o dia (YYYY * 10000 + MM * 100 + DD).

## Sintaxe do Analyze

```python
func.to_yyyymmdd(<expr>)
```

## Exemplos do Analyze

```python
func.to_yyyymmdd('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ func.to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                       │
├────────────────────────────────────────────────┤
│                                       20231112 │
└────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_YYYYMMDD(<expr>)
```

## Argumentos

| Argumentos | Descrição     |
|-----------|---------------|
| `<expr>`  | data/datetime |

## Tipo de retorno

`INT`, retorna no formato `YYYYMMDD`.

## Exemplos de SQL

```sql
SELECT
  to_yyyymmdd('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────┐
│ to_yyyymmdd('2023-11-12 09:38:18.165575') │
│                   UInt32                  │
├───────────────────────────────────────────┤
│                                  20231112 │
└───────────────────────────────────────────┘
```
