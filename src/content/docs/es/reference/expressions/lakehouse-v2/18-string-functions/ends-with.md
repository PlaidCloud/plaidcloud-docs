---
title: ENDS_WITH (Lakehouse v2)
description: ENDS_WITH — Comprueba si una cadena termina con un sufijo especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ends-with.md
---

Comprueba si una cadena termina con un sufijo especificado.

## Sintaxis de Analyze

```python
func.ends_with(<str>, <suffix>)
```

## Ejemplos de Analyze

```python
func.ends_with('hello world', 'world')

┌───┐
│ 1  │
└───┘
```

## Sintaxis de SQL

```sql
ENDS_WITH(<str>, <suffix>)
```

## Ejemplos de SQL

```sql
SELECT ENDS_WITH('hello world', 'world');

┌───┐
│ 1  │
└───┘
```
