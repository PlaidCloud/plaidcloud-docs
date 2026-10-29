---
title: RIGHT (Lakehouse v1)
description: RIGHT — devuelve los len caracteres situados más a la derecha de la cadena str, o NULL si algún argumento es NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/right.md
---

Devuelve los len caracteres situados más a la derecha de la cadena str, o NULL si algún argumento es NULL.

## Sintaxis de Analyze

```python
func.right(<str>, <len>)
```

## Ejemplos de Analyze

```python
func.right('foobarbar', 4)
┌────────────────────────────┐
│ func.right('foobarbar', 4) │
├────────────────────────────┤
│ rbar                       │
└────────────────────────────┘
```

## Sintaxis SQL

```sql
RIGHT(<str>, <len>);
```

## Argumentos

| Argumentos | Descripción                                              |
|-----------|----------------------------------------------------------|
| `<str>`   | La cadena principal de la que se extraen los caracteres |
| `<len>`   | El número de caracteres                                  |

## Tipo de retorno

`VARCHAR`

## Ejemplos de SQL

```sql
SELECT RIGHT('foobarbar', 4);
┌───────────────────────┐
│ RIGHT('foobarbar', 4) │
├───────────────────────┤
│ rbar                  │
└───────────────────────┘
```
