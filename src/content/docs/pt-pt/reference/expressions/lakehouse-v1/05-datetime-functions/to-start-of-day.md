---
title: TO_START_OF_DAY (Lakehouse v1)
description: TO_START_OF_DAY — arredonda por defeito uma data com hora (timestamp/datetime) para o início do dia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-day.md
---

Arredonda por defeito uma data com hora (timestamp/datetime) para o início do dia.

## Sintaxe do Analyze

```python
func.to_start_of_day(<expr>)
```

## Exemplos do Analyze

```python
func.to_start_of_day('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ func.to_start_of_day('2023-11-12 09:38:18.165575') │
│                     Timestamp                      │
├────────────────────────────────────────────────────┤
│ 2023-11-12 00:00:00                                │
└────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_START_OF_DAY( <expr> )
```

## Argumentos

| Argumentos | Descrição            |
|-----------|----------------------|
| `<expr>`  | carimbo de data/hora |

## Tipo de retorno

`TIMESTAMP`, devolve a data no formato “YYYY-MM-DD hh:mm:ss.ffffff”.

## Exemplos SQL

```sql
SELECT
  to_start_of_day('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────────┐
│ to_start_of_day('2023-11-12 09:38:18.165575') │
│                   Timestamp                   │
├───────────────────────────────────────────────┤
│ 2023-11-12 00:00:00                           │
└───────────────────────────────────────────────┘
```
