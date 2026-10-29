---
title: TO_MONDAY (Lakehouse v1)
description: TO_MONDAY — arredonda por defeito uma data ou data com hora (timestamp/datetime) para a segunda-feira mais próxima.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-monday.md
---

Arredonda por defeito uma data ou data com hora (timestamp/datetime) para a segunda-feira mais próxima.
Devolve a data.

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
| `<expr>` | data/carimbo de data/hora |

## Tipo de retorno

`DATE`, devolve a data no formato “YYYY-MM-DD”.

## Exemplos SQL

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
