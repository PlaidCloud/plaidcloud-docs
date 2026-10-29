---
title: PERCENTILE_HASH (Lakehouse v2)
description: PERCENTILE_HASH — calcula um estado de percentil a partir de um valor numérico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-hash.md
---

Calcula um estado de percentil a partir de um valor numérico.

## Sintaxe do Analyze

```python
func.percentile_hash(<value>)
```

## Exemplos do Analyze

```python
func.percentile_hash(42.5)

┌─────────┐
│ (state)  │
└─────────┘
```

## Sintaxe SQL

```sql
PERCENTILE_HASH(<value>)
```

## Exemplos de SQL

```sql
SELECT PERCENTILE_HASH(42.5);

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```
