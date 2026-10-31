---
title: REPLACE (Lakehouse v1)
description: REPLACE — devuelve la cadena str con todas las apariciones de la cadena from_str reemplazadas por la cadena to_str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/replace.md
---

Devuelve la cadena str con todas las apariciones de la cadena from_str reemplazadas por la cadena to_str.

## Sintaxis de Analyze

```python
func.replace(<str>, <from_str>, <to_str>)
```

## Ejemplos de Analyze

```python
func.replace(<str>, <from_str>, <to_str>)
┌──────────────────────────────────────┐
│ func.replace('plaidCloud', 'p', 'P') │
├──────────────────────────────────────┤
│ PlaidCloud                           │
└──────────────────────────────────────┘
```

## Sintaxis SQL

```sql
REPLACE(<str>, <from_str>, <to_str>)
```

## Argumentos

| Argumentos    | Descripción      |
|--------------|------------------|
| `<str>`      | La cadena.      |
| `<from_str>` | La cadena de origen. |
| `<to_str>`   | La cadena de destino.   |

## Tipo de retorno

`VARCHAR`

## Ejemplos de SQL

```sql
SELECT REPLACE('www.mysql.com', 'w', 'Ww');
┌─────────────────────────────────────┐
│ REPLACE('www.mysql.com', 'w', 'Ww') │
├─────────────────────────────────────┤
│ WwWwWw.mysql.com                    │
└─────────────────────────────────────┘
```
