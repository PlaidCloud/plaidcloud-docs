---
title: TO_MONDAY (Lakehouse v1)
description: TO_MONDAY — arredonda para baixo uma data ou data com hora (timestamp/datetime) até a segunda-feira mais próxima.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-monday.md
---

Arredonda para baixo uma data ou data com hora (timestamp/datetime) até a segunda-feira mais próxima.
Retorna a data.

## Sintaxe do Analyze

```python
func.to_monday(<expr>)
```

## Exemplos do Analyze

```python
func.to_monday('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_monday('2023-11-12 09:38:18.165575')       │
│                      Date                          │
├────────────────────────────────────────────────────┤
│ 2023-11-06                                         │
└────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_MONDAY(<expr>)
```

## Argumentos

| Argumentos  | Descrição   |
| ----------- | ----------- |
| `<expr>` | data/timestamp |

## Tipo de retorno

`DATE`, retorna a data no formato “YYYY-MM-DD”.

## Exemplos de SQL

```sql
SELECT
    to_monday('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────┐
│ to_monday('2023-11-12 09:38:18.165575') │
│                   Date                  │
├─────────────────────────────────────────┤
│ 2023-11-06                              │
└─────────────────────────────────────────┘
```
