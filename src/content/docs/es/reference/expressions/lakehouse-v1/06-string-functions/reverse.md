---
title: REVERSE (Lakehouse v1)
description: REVERSE — devuelve la cadena str con el orden de los caracteres invertido.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/reverse.md
---

Devuelve la cadena str con el orden de los caracteres invertido.

## Sintaxis de Analyze

```python
func.reverse(<str>)
```

## Ejemplos de Analyze

```python
func.reverse('abc')
┌──────────────────────┐
│ func..reverse('abc') │
├──────────────────────┤
│ cba                  │
└──────────────────────┘
```

## Sintaxis SQL

```sql
REVERSE(<str>)
```

## Argumentos

| Argumentos | Descripción       |
|-----------|-------------------|
| `<str>`   | El valor de cadena. |

## Tipo de retorno

`VARCHAR`

## Ejemplos de SQL

```sql
SELECT REVERSE('abc');
┌────────────────┐
│ REVERSE('abc') │
├────────────────┤
│ cba            │
└────────────────┘
```
