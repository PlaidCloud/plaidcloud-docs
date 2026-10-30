---
title: OCT (Lakehouse v1)
description: OCT — devuelve una representación en cadena del valor octal de N.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/oct.md
---

Devuelve una representación en cadena del valor octal de N.

## Sintaxis de Analyze

```python
func.oct(<expr>)
```

## Ejemplos de Analyze

```python
func.oct(12)
┌─────────────────┐
│ func.oct(12)    │
├─────────────────┤
│ 014             │
└─────────────────┘
```

## Sintaxis SQL

```sql
OCT(<expr>)
```

## Ejemplos de SQL

```sql
SELECT OCT(12);
┌─────────┐
│ OCT(12) │
├─────────┤
│ 014     │
└─────────┘
```
