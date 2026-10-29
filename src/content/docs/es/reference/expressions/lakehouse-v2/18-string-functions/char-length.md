---
title: CHAR_LENGTH (Lakehouse v2)
description: CHAR_LENGTH — Devuelve el número de caracteres de una cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/char-length.md
---

Devuelve el número de caracteres de una cadena.

## Sintaxis de Analyze

```python
func.char_length(<str>)
```

## Ejemplos de Analyze

```python
func.char_length('hello world')

┌────┐
│ 11  │
└────┘
```

## Sintaxis de SQL

```sql
CHAR_LENGTH(<str>)
```

## Ejemplos de SQL

```sql
SELECT CHAR_LENGTH('hello world');

┌────┐
│ 11  │
└────┘
```
