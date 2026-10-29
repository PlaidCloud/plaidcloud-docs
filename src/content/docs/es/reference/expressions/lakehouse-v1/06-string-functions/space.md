---
title: SPACE (Lakehouse v1)
description: SPACE — devuelve una cadena formada por N caracteres de espacio en blanco.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/space.md
---

Devuelve una cadena formada por N caracteres de espacio en blanco.

## Sintaxis de Analyze

```python
func.space(<n>)
```

## Ejemplos de Analyze

```python
func.space(20)
┌─────────────────┐
│ func.space(20)  │
├─────────────────┤
│                 │
└─────────────────┘
```

## Sintaxis SQL

```sql
SPACE(<n>);
```

## Argumentos

| Argumentos | Descripción          |
|-----------|----------------------|
| `<n>`     | El número de espacios |

## Tipo de retorno

Valor de tipo de datos de cadena.

## Ejemplos de SQL

```sql
SELECT SPACE(20)
┌──────────────────────┐
│ SPACE(20)            │
├──────────────────────┤
│                      │
└──────────────────────┘
```
