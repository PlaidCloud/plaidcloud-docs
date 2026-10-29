---
title: TO_VARIANT (Lakehouse v1)
description: "TO_VARIANT : convertit une valeur en type de données VARIANT."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/to-variant.md
---

Convertit une valeur en type de données VARIANT.

## Syntaxe Analyze

```python
func.to_variant( <expr> )
```

## Exemples Analyze

```python
func.to_variant(to_bitmap('100,200,300'))

┌───────────────────────────────────────────┐
│ func.to_variant(to_bitmap('100,200,300')) │
├───────────────────────────────────────────┤
│ [100,200,300]                             │
└───────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
TO_VARIANT( <expr> )
```

## Exemples SQL

```sql
SELECT TO_VARIANT(TO_BITMAP('100,200,300'));

┌──────────────────────────────────────┐
│ to_variant(to_bitmap('100,200,300')) │
├──────────────────────────────────────┤
│ [100,200,300]                        │
└──────────────────────────────────────┘
```
