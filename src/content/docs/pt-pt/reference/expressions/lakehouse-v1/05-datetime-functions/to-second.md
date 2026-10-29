---
title: TO_SECOND (Lakehouse v1)
description: TO_SECOND — converte uma data com hora (timestamp/datetime) num número UInt8 que contém o segundo do minuto (0-59).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-second.md
---

Converte uma data com hora (timestamp/datetime) num número UInt8 que contém o segundo do minuto (0-59).

## Sintaxe do Analyze

```python
func.to_second(<expr>)
```

## Exemplos do Analyze

```python
func.to_second('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────┐
│ func.to_second('2023-11-12 09:38:18.165575') │
│                   UInt8                      │
├──────────────────────────────────────────────┤
│                                           18 │
└──────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_SECOND(<expr>)
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
    to_second('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_second('2023-11-12 09:38:18.165575') │
│                  UInt8                  │
├─────────────────────────────────────────┤
│                                      18 │
└─────────────────────────────────────────┘
```
