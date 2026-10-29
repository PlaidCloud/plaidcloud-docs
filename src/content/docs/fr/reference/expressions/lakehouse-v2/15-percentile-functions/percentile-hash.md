---
title: PERCENTILE_HASH (Lakehouse v2)
description: PERCENTILE_HASH — calcule un état de centile à partir d'une valeur numérique.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-hash.md
---

Calcule un état de centile à partir d'une valeur numérique.

## Syntaxe Analyze

```python
func.percentile_hash(<value>)
```

## Exemples Analyze

```python
func.percentile_hash(42.5)

┌─────────┐
│ (state)  │
└─────────┘
```

## Syntaxe SQL

```sql
PERCENTILE_HASH(<value>)
```

## Exemples SQL

```sql
SELECT PERCENTILE_HASH(42.5);

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```
