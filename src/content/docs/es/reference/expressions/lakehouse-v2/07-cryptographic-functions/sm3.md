---
title: SM3 (Lakehouse v2)
description: SM3 — devuelve el hash SM3 de una cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/sm3.md
---

Devuelve el hash SM3 de una cadena.

## Sintaxis de Analyze

```python
func.sm3(<str>)
```

## Ejemplos de Analyze

```python
func.sm3('hello')

┌───────────────┐
│ 'becbbfaa...'  │
└───────────────┘
```

## Sintaxis de SQL

```sql
SM3(<str>)
```

## Ejemplos de SQL

```sql
SELECT SM3('hello');

┌──────────────────────────────────────────────────────────────────┐
│ becbbfaae6548b8bf0cfcad5a27183cd1be6093b1cceccc303d9c61d0a645268  │
└──────────────────────────────────────────────────────────────────┘
```
