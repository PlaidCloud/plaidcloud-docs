---
title: CHAR (Lakehouse v2)
description: CHAR — Devuelve el carácter correspondiente a un código ASCII dado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/char.md
---

Devuelve el carácter correspondiente a un código ASCII dado.

## Sintaxis de Analyze

```python
func.char(<code>)
```

## Ejemplos de Analyze

```python
func.char(65)

┌─────┐
│ 'A'  │
└─────┘
```

## Sintaxis de SQL

```sql
CHAR(<code>)
```

## Ejemplos de SQL

```sql
SELECT CHAR(65);

┌───┐
│ A  │
└───┘
```
