---
title: TO_START_OF_ISO_YEAR (Lakehouse v1)
description: TO_START_OF_ISO_YEAR — devolve o primeiro dia do ano ISO de uma data ou de uma data com hora.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-iso-year.md
---

Devolve o primeiro dia do ano ISO de uma data ou de uma data com hora (timestamp/datetime).

## Sintaxe do Analyze

```python
func.to_start_of_iso_year(<expr>)
```

## Exemplos do Analyze

```python
func.to_start_of_iso_year('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_iso_year('2023-11-12 09:38:18.165575')        │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-01-02                                                     │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_START_OF_ISO_YEAR(<expr>)
```

## Argumentos

| Argumentos | Descrição            |
|-----------|----------------------|
| `<expr>`  | data/carimbo de data/hora |

## Tipo de retorno

`DATE`, devolve a data no formato “YYYY-MM-DD”.

## Exemplos SQL

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
