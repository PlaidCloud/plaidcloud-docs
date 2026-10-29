---
title: RPAD (Lakehouse v2)
description: RPAD — Rellena una cadena por la derecha hasta una longitud especificada con una cadena de relleno.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/rpad.md
---

Rellena una cadena por la derecha hasta una longitud especificada con una cadena de relleno.

## Sintaxis de Analyze

```python
func.rpad(<str>, <len>, <pad>)
```

## Ejemplos de Analyze

```python
func.rpad('hello', 10, '.')

┌──────────────┐
│ 'hello.....'  │
└──────────────┘
```

## Sintaxis de SQL

```sql
RPAD(<str>, <len>, <pad>)
```

## Ejemplos de SQL

```sql
SELECT RPAD('hello', 10, '.');

┌────────────┐
│ hello.....  │
└────────────┘
```
