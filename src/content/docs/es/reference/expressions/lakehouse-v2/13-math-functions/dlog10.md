---
title: DLOG10 (Lakehouse v2)
description: DLOG10 — alias de `LOG10`. Consulte [LOG10](../log10/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dlog10.md
---

Alias de `LOG10`. Consulte [LOG10](../log10/).

## Sintaxis de Analyze

```python
func.dlog10(1000)
```

## Ejemplos de Analyze

```python
func.dlog10(1000)

┌─────┐
│ 3.0 │
└─────┘
```

## Sintaxis de SQL

```sql
DLOG10(<x>)
```

## Ejemplos de SQL

```sql
SELECT DLOG10(1000);

┌─────┐
│ 3.0 │
└─────┘
```
