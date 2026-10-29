---
title: TO_HOUR (Lakehouse v1)
description: TO_HOUR — converte uma data com hora (timestamp/datetime) num número UInt8 que contém a hora no formato de 24 horas (0-23).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-hour.md
---

Converte uma data com hora (timestamp/datetime) num número UInt8 que contém a hora no formato de 24 horas (0-23).
Esta função pressupõe que, quando os relógios são adiantados, o ajuste é de uma hora e ocorre às 2 h e, quando são atrasados, o ajuste é de uma hora e ocorre às 3 h (o que nem sempre é verdade – mesmo em Moscovo, os relógios foram alterados duas vezes em momentos diferentes).


## Sintaxe do Analyze

```python
func.to_hour(<expr>)
```

## Exemplos do Analyze

```python
func.to_hour('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_hour('2023-11-12 09:38:18.165575')         │
│                     UInt8                          │
├────────────────────────────────────────────────────┤
│                                                  9 │
└────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_HOUR(<expr>)
```

## Argumentos

| Argumentos | Descrição            |
|-----------|----------------------|
| `<expr>`  | carimbo de data/hora |

## Tipo de retorno

`TINYINT`

## Exemplos SQL

```sql
SELECT
    to_hour('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────┐
│ to_hour('2023-11-12 09:38:18.165575') │
│                 UInt8                 │
├───────────────────────────────────────┤
│                                     9 │
└───────────────────────────────────────┘
```
