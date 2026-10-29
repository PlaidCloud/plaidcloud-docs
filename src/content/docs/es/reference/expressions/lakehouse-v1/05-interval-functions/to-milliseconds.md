---
title: TO_MILLISECONDS (Lakehouse v1)
description: TO_MILLISECONDS — convierte un número determinado de milisegundos en un tipo Interval.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-milliseconds.md
---

Convierte un número determinado de milisegundos en un tipo Interval.

- Acepta como entrada enteros positivos, cero y enteros negativos.

## Sintaxis de Analyze

```python
func.to_milliseconds(<milliseconds>)
```

## Ejemplos de Analyze

```python
func.to_milliseconds(2)
┌──────────────────────────────────────────────────────┐
│ func.to_milliseconds(2)                              │
├──────────────────────────────────────────────────────┤
│  0:00:00.002                                         │
└──────────────────────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TO_MILLISECONDS(<milliseconds>)
```

## Tipo de retorno

Interval (con el formato `hh:mm:ss.sss`).

## Ejemplos de SQL

```sql
SELECT TO_MILLISECONDS(2), TO_MILLISECONDS(0), TO_MILLISECONDS((- 2));

┌────────────────────────────────────────────────────────────────┐
│ to_milliseconds(2) │ to_milliseconds(0) │ to_milliseconds(- 2) │
├────────────────────┼────────────────────┼──────────────────────┤
│ 0:00:00.002        │ 00:00:00           │ -0:00:00.002         │
└────────────────────────────────────────────────────────────────┘
```
