---
title: INSTR (Lakehouse v2)
description: INSTR — Devuelve la posición de la primera aparición de una subcadena en una cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/instr.md
---

Devuelve la posición de la primera aparición de una subcadena en una cadena.

## Sintaxis de Analyze

```python
func.instr(<str>, <substr>)
```

## Ejemplos de Analyze

```python
func.instr('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## Sintaxis de SQL

```sql
INSTR(<str>, <substr>)
```

## Ejemplos de SQL

```sql
SELECT INSTR('hello world', 'world');

┌───┐
│ 7  │
└───┘
```
