---
title: TO_START_OF_QUARTER (Lakehouse v1)
description: TO_START_OF_QUARTER — arredonda para baixo uma data ou data com hora (timestamp/datetime) para o primeiro dia do trimestre.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-start-of-quarter.md
---

Arredonda para baixo uma data ou data com hora (timestamp/datetime) para o primeiro dia do trimestre.
O primeiro dia do trimestre é 1 de janeiro, 1 de abril, 1 de julho ou 1 de outubro.
Devolve a data.

## Sintaxe do Analyze

```python
func.to_start_of_quarter(<expr>)
```

## Exemplos do Analyze

```python
func.to_start_of_quarter('2023-11-12 09:38:18.165575')

┌────────────────────────────────────────────────────────────────┐
│ func.to_start_of_quarter('2023-11-12 09:38:18.165575')         │
│                          Date                                  │
├────────────────────────────────────────────────────────────────┤
│ 2023-10-01                                                     │
└────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TO_START_OF_QUARTER(<expr>)
```

## Argumentos

| Argumentos | Descrição      |
|-----------|----------------|
| `<expr>`   | data/timestamp |

## Tipo de Retorno

`DATE`, devolve a data no formato “YYYY-MM-DD”.

## Exemplos SQL

```sql
SELECT
  to_start_of_quarter('2023-11-12 09:38:18.165575')

┌───────────────────────────────────────────────────┐
│ to_start_of_quarter('2023-11-12 09:38:18.165575') │
│                        Date                       │
├───────────────────────────────────────────────────┤
│ 2023-10-01                                        │
└───────────────────────────────────────────────────┘
```
