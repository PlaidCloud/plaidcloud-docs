---
title: TO_START_OF_WEEK (Lakehouse v1)
description: TO_START_OF_WEEK — devuelve el primer día de la semana para una fecha o una fecha con hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-week.md
---

Devuelve el primer día de la semana para una fecha o una fecha con hora (marca de tiempo/datetime).
El primer día de la semana puede ser domingo o lunes, según lo especifique el argumento `mode`.

## Sintaxis de Analyze

```python
func.to_start_of_week(<expr>)
```

## Ejemplos de Analyze

```python
func.to_start_of_week('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_week('2023-11-12 09:38:18.165575')            │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-11-12                                                     │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_START_OF_WEEK(<expr> [, mode])
```

## Argumentos

| Argumentos | Descripción                                                                                         |
|-----------|-----------------------------------------------------------------------------------------------------|
| `<expr>`  | fecha/marca de tiempo                                                                                      |
| `[mode]`  | Opcional. Si es 0, el resultado es domingo; de lo contrario, el resultado es lunes. El valor predeterminado es 0 |

## Tipo de retorno

`DATE`, devuelve la fecha en formato “YYYY-MM-DD”.

## Ejemplos de SQL

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
