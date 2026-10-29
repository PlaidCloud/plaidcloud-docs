---
title: TRUNCATE (Lakehouse v2)
description: TRUNCATE — trunca un número a un número específico de decimales.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/truncate.md
---

Trunca un número a un número específico de decimales.

## Sintaxis de Analyze

```python
func.truncate(<x>, <d>)
```

## Ejemplos de Analyze

```python
func.truncate(3.14159, 2)

┌──────┐
│ 3.14  │
└──────┘
```

## Sintaxis de SQL

```sql
TRUNCATE(<x>, <d>)
```

## Ejemplos de SQL

```sql
SELECT TRUNCATE(3.14159, 2);

┌──────┐
│ 3.14  │
└──────┘
```
