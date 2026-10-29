---
title: TO_MINUTE (Lakehouse v1)
description: TO_MINUTE — converte uma data com hora (timestamp/datetime) em um número UInt8 que contém o minuto da hora (0-59).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-minute.md
---

Converte uma data com hora (timestamp/datetime) em um número UInt8 que contém o minuto da hora (0-59).


## Sintaxe do Analyze

```python
func.to_minute(<expr>)
```

## Exemplos do Analyze

```python
func.to_minute('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_minute('2023-11-12 09:38:18.165575')       │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                 38 │
└────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_MINUTE(<expr>)
```

## Argumentos

| Argumentos | Descrição   |
|-----------|-------------|
| `<expr>`  | timestamp   |

## Tipo de retorno

 `TINYINT`

## Exemplos de SQL

```sql
SELECT
    to_minute('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_minute('2023-11-12 09:38:18.165575') │
│                  UInt8                  │
├─────────────────────────────────────────┤
│                                      38 │
└─────────────────────────────────────────┘
```
