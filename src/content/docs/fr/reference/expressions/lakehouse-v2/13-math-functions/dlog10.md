---
title: DLOG10 (Lakehouse v2)
description: DLOG10 — alias de `LOG10`. Voir [LOG10](../log10/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dlog10.md
---

Alias de `LOG10`. Voir [LOG10](../log10/).

## Syntaxe Analyze

```python
func.dlog10(1000)
```

## Exemples Analyze

```python
func.dlog10(1000)

┌─────┐
│ 3.0 │
└─────┘
```

## Syntaxe SQL

```sql
DLOG10(<x>)
```

## Exemples SQL

```sql
SELECT DLOG10(1000);

┌─────┐
│ 3.0 │
└─────┘
```
