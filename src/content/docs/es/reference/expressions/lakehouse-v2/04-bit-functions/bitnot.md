---
title: BITNOT (Lakehouse v2)
description: BITNOT — devuelve el NOT bit a bit de un valor numérico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitnot.md
---

Devuelve el NOT bit a bit de un valor numérico.

## Sintaxis de Analyze

```python
func.bitnot(<x>)
```

## Ejemplos de Analyze

```python
func.bitnot(0)

┌──────┐
│ '-1'  │
└──────┘
```

## Sintaxis de SQL

```sql
BITNOT(<x>)
```

## Ejemplos de SQL

```sql
SELECT BITNOT(0);

┌────┐
│ -1  │
└────┘
```
