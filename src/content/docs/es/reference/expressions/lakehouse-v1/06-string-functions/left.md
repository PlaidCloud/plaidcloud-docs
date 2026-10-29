---
title: LEFT (Lakehouse v1)
description: LEFT — devuelve los len caracteres situados más a la izquierda de la cadena str, o NULL si algún argumento es NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/left.md
---

Devuelve los len caracteres situados más a la izquierda de la cadena str, o NULL si algún argumento es NULL.

## Sintaxis de Analyze

```python
func.left(<str>, <len>)
```

## Ejemplos de Analyze

```python
func.left('foobarbar', 5)
┌───────────────────────────┐
│ func.left('foobarbar', 5) │
├───────────────────────────┤
│ fooba                     │
└───────────────────────────┘
```

## Sintaxis SQL

```sql
LEFT(<str>, <len>);
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
SELECT LEFT('foobarbar', 5);
┌──────────────────────┐
│ LEFT('foobarbar', 5) │
├──────────────────────┤
│ fooba                │
└──────────────────────┘
```
