---
title: LOG (Lakehouse v2)
description: LOG — devuelve el logaritmo de un número en una base específica.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log.md
---

Devuelve el logaritmo de un número en una base específica.

## Sintaxis de Analyze

```python
func.log(<base>, <x>)
```

## Ejemplos de Analyze

```python
func.log(10, 100)

┌─────┐
│ 2.0  │
└─────┘
```

## Sintaxis de SQL

```sql
LOG(<base>, <x>)
```

## Ejemplos de SQL

```sql
SELECT LOG(10, 100);

┌─────┐
│ 2.0  │
└─────┘
```
