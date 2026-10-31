---
title: ASCII (Lakehouse v2)
description: ASCII — Devuelve el código ASCII del primer carácter de una cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ascii.md
---

Devuelve el código ASCII del primer carácter de una cadena.

## Sintaxis de Analyze

```python
func.ascii(<str>)
```

## Ejemplos de Analyze

```python
func.ascii('A')

┌────┐
│ 65  │
└────┘
```

## Sintaxis de SQL

```sql
ASCII(<str>)
```

## Ejemplos de SQL

```sql
SELECT ASCII('A');

┌────┐
│ 65  │
└────┘
```
