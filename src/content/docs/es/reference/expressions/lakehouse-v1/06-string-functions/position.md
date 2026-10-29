---
title: POSITION (Lakehouse v1)
description: POSITION — POSITION(substr IN str) es un sinónimo de LOCATE(substr,str).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/position.md
---

POSITION(substr IN str) es un sinónimo de LOCATE(substr,str).
Devuelve la posición de la primera aparición de la subcadena substr en la cadena str.
Devuelve 0 si substr no está en str. Devuelve NULL si algún argumento es NULL.

## Sintaxis de Analyze

```python
func.position(<substr>, <str>)
```

## Ejemplos de Analyze

```python
func.position('bar', 'foobarbar')
┌───────────────────────────────────┐
│ func.position('bar', 'foobarbar') │
├───────────────────────────────────┤
│                                 4 │
└───────────────────────────────────┘
```

## Sintaxis SQL

```sql
POSITION(<substr> IN <str>)
```

## Argumentos

| Argumentos  | Descripción    |
|------------|----------------|
| `<substr>` | La subcadena. |
| `<str>`    | La cadena.    |

## Tipo de retorno

`BIGINT`

## Ejemplos de SQL

```sql
SELECT POSITION('bar' IN 'foobarbar')
┌────────────────────────────┐
│ POSITION('bar' IN 'foobarbar') │
├────────────────────────────┤
│                          4 │
└────────────────────────────┘

SELECT POSITION('xbar' IN 'foobar')
┌──────────────────────────┐
│ POSITION('xbar' IN 'foobar') │
├──────────────────────────┤
│                        0 │
└──────────────────────────┘
```
