---
title: CONCAT (Lakehouse v2)
description: CONCAT — concatène deux chaînes ou plus.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/concat.md
---

Concatène deux chaînes ou plus.

## Syntaxe Analyze

```python
func.concat(<str1>, <str2>[, ...])
```

## Exemples Analyze

```python
func.concat('Star', 'Rocks')

┌─────────────┐
│ 'StarRocks'  │
└─────────────┘
```

## Syntaxe SQL

```sql
CONCAT(<str1>, <str2>[, ...])
```

## Exemples SQL

```sql
SELECT CONCAT('Star', 'Rocks');

┌───────────┐
│ StarRocks  │
└───────────┘
```
