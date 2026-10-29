---
title: TO_START_OF_HOUR (Lakehouse v1)
description: TO_START_OF_HOUR — arredonda por defeito uma data com hora (timestamp/datetime) para o início da hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-hour.md
---

Arredonda por defeito uma data com hora (timestamp/datetime) para o início da hora.

## Sintaxe do Analyze

```python
func.to_start_of_hour(<expr>)
```

## Exemplos do Analyze

```python
func.to_start_of_hour('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_hour('2023-11-12 09:38:18.165575')            │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:00:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_START_OF_HOUR(<expr>)
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
  to_start_of_hour('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ to_start_of_hour('2023-11-12 09:38:18.165575') │
│                    Timestamp                   │
├────────────────────────────────────────────────┤
│ 2023-11-12 09:00:00                            │
└────────────────────────────────────────────────┘
```
