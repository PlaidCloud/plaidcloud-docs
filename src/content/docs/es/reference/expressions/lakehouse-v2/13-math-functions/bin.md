---
title: BIN (Lakehouse v2)
description: BIN — devuelve la representación binaria en cadena de un entero.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/bin.md
---

Devuelve la representación binaria en cadena de un entero.

## Sintaxis de Analyze

```python
func.bin(<x>)
```

## Ejemplos de Analyze

```python
func.bin(10)

┌────────┐
│ '1010'  │
└────────┘
```

## Sintaxis de SQL

```sql
BIN(<x>)
```

## Ejemplos de SQL

```sql
SELECT BIN(10);

┌──────┐
│ 1010  │
└──────┘
```
