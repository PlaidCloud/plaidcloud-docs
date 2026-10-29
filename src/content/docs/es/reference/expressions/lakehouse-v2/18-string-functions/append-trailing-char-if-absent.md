---
title: APPEND_TRAILING_CHAR_IF_ABSENT (Lakehouse v2)
description: "Use la función de cadena APPEND_TRAILING_CHAR_IF_ABSENT en PlaidCloud Lakehouse. Agrega un carácter final a una cadena si aún no está presente."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/append-trailing-char-if-absent.md
---

Agrega un carácter final a una cadena si aún no está presente.

## Sintaxis de Analyze

```python
func.append_trailing_char_if_absent(<str>, <char>)
```

## Ejemplos de Analyze

```python
func.append_trailing_char_if_absent('hello', '!')

┌──────────┐
│ 'hello!'  │
└──────────┘
```

## Sintaxis de SQL

```sql
APPEND_TRAILING_CHAR_IF_ABSENT(<str>, <char>)
```

## Ejemplos de SQL

```sql
SELECT APPEND_TRAILING_CHAR_IF_ABSENT('hello', '!');

┌────────┐
│ hello!  │
└────────┘
```
