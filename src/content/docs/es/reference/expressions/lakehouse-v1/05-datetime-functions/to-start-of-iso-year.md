---
title: TO_START_OF_ISO_YEAR (Lakehouse v1)
description: TO_START_OF_ISO_YEAR — devuelve el primer día del año ISO de una fecha o de una fecha con hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-iso-year.md
---

Devuelve el primer día del año ISO de una fecha o de una fecha con hora (marca de tiempo/datetime).

## Sintaxis de Analyze

```python
func.to_start_of_iso_year(<expr>)
```

## Ejemplos de Analyze

```python
func.to_start_of_iso_year('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_iso_year('2023-11-12 09:38:18.165575')        │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-01-02                                                     │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TO_START_OF_ISO_YEAR(<expr>)
```

## Argumentos

| Argumentos | Descripción    |
|-----------|----------------|
| `<expr>`  | fecha/marca de tiempo |

## Tipo de valor devuelto

`DATE`, devuelve la fecha en el formato “YYYY-MM-DD”.

## Ejemplos de SQL

```sql
SELECT
  to_start_of_iso_year('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────┐
│ to_start_of_iso_year('2023-11-12 09:38:18.165575') │
│                        Date                        │
├────────────────────────────────────────────────────┤
│ 2023-01-02                                         │
└────────────────────────────────────────────────────┘
```
