---
title: TO_START_OF_SECOND (Lakehouse v1)
description: TO_START_OF_SECOND — arredonda para baixo uma data com hora (timestamp/datetime) para o início do segundo.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-second.md
---

Arredonda para baixo uma data com hora (timestamp/datetime) para o início do segundo.

## Sintaxe do Analyze

```python
func.to_start_of_second(<expr>)
```

## Exemplos do Analyze

```python
func.to_start_of_second('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_second('2023-11-12 09:38:18.165575')          │
│                          Timestamp                             │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12 09:38:18                                            │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_START_OF_SECOND(<expr>)
```

## Argumentos

| Argumentos | Descrição |
|-----------|-------------|
| `<expr>`  | timestamp   |

## Tipo de retorno

`TIMESTAMP`, retorna a data no formato “YYYY-MM-DD hh:mm:ss.ffffff”.

## Exemplos de SQL

```sql
SELECT
  to_start_of_second('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────┐
│ to_start_of_second('2023-11-12 09:38:18.165575') │
│                     Timestamp                    │
├──────────────────────────────────────────────────┤
│ 2023-11-12 09:38:18                              │
└──────────────────────────────────────────────────┘
```
