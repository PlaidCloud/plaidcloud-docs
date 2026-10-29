---
title: LPAD (Lakehouse v2)
description: LPAD — Rellena una cadena por la izquierda hasta una longitud especificada con una cadena de relleno.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lpad.md
---

Rellena una cadena por la izquierda hasta una longitud especificada con una cadena de relleno.

## Sintaxis de Analyze

```python
func.lpad(<str>, <len>, <pad>)
```

## Ejemplos de Analyze

```python
func.lpad('42', 5, '0')

┌─────────┐
│ '00042'  │
└─────────┘
```

## Sintaxis de SQL

```sql
LPAD(<str>, <len>, <pad>)
```

## Ejemplos de SQL

```sql
SELECT LPAD('42', 5, '0');

┌───────┐
│ 00042  │
└───────┘
```
