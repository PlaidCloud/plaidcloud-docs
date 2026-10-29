---
title: TO_START_OF_FIFTEEN_MINUTES (Lakehouse v1)
description: TO_START_OF_FIFTEEN_MINUTES — arredonda por defeito a data com hora (timestamp/datetime) para o início do intervalo de quinze minutos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-fifteen-minutes.md
---

Arredonda por defeito a data com hora (timestamp/datetime) para o início do intervalo de quinze minutos.

## Sintaxe do Analyze

```python
func.to_start_of_fifteen_minutes(<expr>)
```

## Exemplos do Analyze

```python
func.to_start_of_fifteen_minutes('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_fifteen_minutes('2023-11-12 09:38:18.165575') │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:30:00                                            │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_START_OF_FIFTEEN_MINUTES(<expr>)
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
  to_start_of_fifteen_minutes('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────────────────────┐
│ to_start_of_fifteen_minutes('2023-11-12 09:38:18.165575') │
│                         Timestamp                         │
├───────────────────────────────────────────────────────────┤
│ 2023-11-12 09:30:00                                       │
└───────────────────────────────────────────────────────────┘
```
