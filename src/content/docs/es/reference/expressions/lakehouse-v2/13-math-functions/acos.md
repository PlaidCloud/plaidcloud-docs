---
title: ACOS (Lakehouse v2)
description: ACOS — devuelve el arcocoseno de un número en radianes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/acos.md
---

Devuelve el arcocoseno de un número en radianes.

## Sintaxis de Analyze

```python
func.acos(<x>)
```

## Ejemplos de Analyze

```python
func.acos(0.5)

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```

## Sintaxis de SQL

```sql
ACOS(<x>)
```

## Ejemplos de SQL

```sql
SELECT ACOS(0.5);

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```
