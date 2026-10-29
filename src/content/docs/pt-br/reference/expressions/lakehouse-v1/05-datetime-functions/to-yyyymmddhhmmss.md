---
title: TO_YYYYMMDDHHMMSS (Lakehouse v1)
description: TO_YYYYMMDDHHMMSS — converte uma data ou data com hora (timestamp/datetime) em um número UInt64.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmddhhmmss.md
---

Converte uma data ou data com hora (timestamp/datetime) em um número UInt64 que contém o ano, o mês, o dia, a hora, os minutos e os segundos (YYYY * 10000000000 + MM * 100000000 + DD * 1000000 + hh * 10000 + mm * 100 + ss).

## Sintaxe do Analyze

```python
func.to_yyyymmddhhmmss(<expr>)
```

## Exemplos do Analyze

```python
func.to_yyyymmddhhmmss('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────────┐
│ func.to_yyyymmddhhmmss('2023-11-12 09:38:18.165575') │
│                   UInt64                             │
├──────────────────────────────────────────────────────┤
│                                       20231112092818 │
└──────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_YYYYMMDDHHMMSS(<expr>)
```

## Argumentos

| Argumentos | Descrição      |
|-----------|----------------|
| `<expr>`  | data/timestamp |

## Tipo de retorno

`BIGINT`, retorna no formato `YYYYMMDDhhmmss`.

## Exemplos de SQL

```sql
SELECT
  to_yyyymmddhhmmss('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────────┐
│ to_yyyymmddhhmmss('2023-11-12 09:38:18.165575') │
│                      UInt64                     │
├─────────────────────────────────────────────────┤
│                                  20231112092818 │
└─────────────────────────────────────────────────┘
```
