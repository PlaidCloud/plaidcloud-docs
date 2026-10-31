---
title: TO_YYYYMMDDHH (Lakehouse v1)
description: TO_YYYYMMDDHH — da formato a una fecha o marca de tiempo como una cadena con el formato YYYYMMDDHH.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/to-yyyymmddhh.md
---

Da formato a una fecha o marca de tiempo como una representación de cadena con el formato "YYYYMMDDHH" (año, mes, día, hora).

## Sintaxis de Analyze

```python
func.to_yyyymmddhh(<expr>)
```

## Ejemplos de Analyze

```python
func.to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌──────────────────────────────────────────────────┐
│ func.to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                   UInt32                         │
├──────────────────────────────────────────────────┤
│                                       2023111209 │
└──────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_YYYYMMDDHH(<expr>)
```

## Argumentos

| Argumentos | Descripción   |
|-----------|---------------|
| `<expr>`  | fecha/datetime |

## Tipo de retorno

Devuelve un entero de 64 bits sin signo (UInt64) con el formato "YYYYMMDDHH".

## Ejemplos de SQL

```sql
SELECT
  to_yyyymmddhh('2023-11-12 09:38:18.165575')

┌─────────────────────────────────────────────┐
│ to_yyyymmddhh('2023-11-12 09:38:18.165575') │
│                    UInt32                   │
├─────────────────────────────────────────────┤
│                                  2023111209 │
└─────────────────────────────────────────────┘
```
