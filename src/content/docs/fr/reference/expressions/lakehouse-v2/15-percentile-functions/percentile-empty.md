---
title: PERCENTILE_EMPTY (Lakehouse v2)
description: PERCENTILE_EMPTY — renvoie un état de centile vide à des fins d'initialisation.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-empty.md
---

Renvoie un état de centile vide à des fins d'initialisation.

## Syntaxe Analyze

```python
func.percentile_empty()
```

## Exemples Analyze

```python
func.percentile_empty()

┌───────────────┐
│ (empty state)  │
└───────────────┘
```

## Syntaxe SQL

```sql
PERCENTILE_EMPTY()
```

## Exemples SQL

```sql
SELECT PERCENTILE_EMPTY();

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```
