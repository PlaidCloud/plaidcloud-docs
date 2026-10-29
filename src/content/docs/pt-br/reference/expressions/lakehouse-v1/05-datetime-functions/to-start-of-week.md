---
title: TO_START_OF_WEEK (Lakehouse v1)
description: TO_START_OF_WEEK — retorna o primeiro dia da semana de uma data ou data com hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-week.md
---

Retorna o primeiro dia da semana de uma data ou data com hora (timestamp/datetime).
O primeiro dia da semana pode ser domingo ou segunda-feira, conforme especificado pelo argumento `mode`.

## Sintaxe do Analyze

```python
func.to_start_of_week(<expr>)
```

## Exemplos do Analyze

```python
func.to_start_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_week('2023-11-12 09:38:18.165575')            │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12                                                     │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_START_OF_WEEK(<expr> [, mode])
```

## Argumentos

| Argumentos | Descrição                                                                                           |
|-----------|-----------------------------------------------------------------------------------------------------|
| `<expr>`  | data/timestamp                                                                                      |
| `[mode]`  | Opcional. Se for 0, o resultado é domingo; caso contrário, o resultado é segunda-feira. O valor padrão é 0 |

## Tipo de retorno

`DATE`, retorna a data no formato “YYYY-MM-DD”.

## Exemplos de SQL

```sql
SELECT
  to_start_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────┐
│ to_start_of_week('2023-11-12 09:38:18.165575') │
│                      Date                      │
├────────────────────────────────────────────────┤
│ 2023-11-12                                     │
└────────────────────────────────────────────────┘
```
