---
title: REGEXP_EXTRACT (Lakehouse v2)
description: REGEXP_EXTRACT — extrait la première sous-chaîne qui correspond à un motif d'expression régulière.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-extract.md
---

Extrait la première sous-chaîne qui correspond à un motif d'expression régulière.

## Syntaxe Analyze

```python
func.regexp_extract(<str>, <pattern>[, <group>])
```

## Exemples Analyze

```python
func.regexp_extract('price: $42.50', '\\$(\\d+\\.\\d+)', 1)

┌─────────┐
│ '42.50'  │
└─────────┘
```

## Syntaxe SQL

```sql
REGEXP_EXTRACT(<str>, <pattern>[, <group>])
```

## Exemples SQL

```sql
SELECT REGEXP_EXTRACT('price: $42.50', '\\$(\\d+\\.\\d+)', 1);

┌───────┐
│ 42.50  │
└───────┘
```
