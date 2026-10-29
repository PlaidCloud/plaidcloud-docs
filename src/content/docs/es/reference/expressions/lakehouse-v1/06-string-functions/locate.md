---
title: LOCATE (Lakehouse v1)
description: LOCATE — la primera sintaxis devuelve la posición de la primera aparición de la subcadena substr en la cadena str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/locate.md
---

La primera sintaxis devuelve la posición de la primera aparición de la subcadena substr en la cadena str.
La segunda sintaxis devuelve la posición de la primera aparición de la subcadena substr en la cadena str, a partir de la posición pos.
Devuelve 0 si substr no está en str. Devuelve NULL si algún argumento es NULL.

## Sintaxis de Analyze

```python
func.locate(<substr>, <str>, <pos>)
```

## Ejemplos de Analyze

```python
func.locate('bar', 'foobarbar')
┌────────────────────────────────────┐
│ func.locate('bar', 'foobarbar') │
├────────────────────────────────────┤
│                                  5 │
└────────────────────────────────────┘
```

```python
func.locate('bar', 'foobarbar', 5)
┌────────────────────────────────────┐
│ func.locate('bar', 'foobarbar', 5) │
├────────────────────────────────────┤
│                                  7 │
└────────────────────────────────────┘
```

## Sintaxis SQL

```sql
LOCATE(<substr>, <str>)
LOCATE(<substr>, <str>, <pos>)
```

## Argumentos

| Argumentos  | Descripción    |
|------------|----------------|
| `<substr>` | La subcadena. |
| `<str>`    | La cadena.    |
| `<pos>`    | La posición.  |

## Tipo de retorno

`BIGINT`

## Ejemplos de SQL

```sql
SELECT LOCATE('bar', 'foobarbar')
┌────────────────────────────┐
│ LOCATE('bar', 'foobarbar') │
├────────────────────────────┤
│                          4 │
└────────────────────────────┘

SELECT LOCATE('xbar', 'foobar')
┌──────────────────────────┐
│ LOCATE('xbar', 'foobar') │
├──────────────────────────┤
│                        0 │
└──────────────────────────┘

SELECT LOCATE('bar', 'foobarbar', 5)
┌───────────────────────────────┐
│ LOCATE('bar', 'foobarbar', 5) │
├───────────────────────────────┤
│                             7 │
└───────────────────────────────┘
```
