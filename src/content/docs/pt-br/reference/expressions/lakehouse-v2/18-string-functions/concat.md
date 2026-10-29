---
title: CONCAT (Lakehouse v2)
description: CONCAT — concatena duas ou mais strings.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/concat.md
---

Concatena duas ou mais strings.

## Sintaxe do Analyze

```python
func.concat(<str1>, <str2>[, ...])
```

## Exemplos do Analyze

```python
func.concat('Star', 'Rocks')

┌─────────────┐
│ 'StarRocks'  │
└─────────────┘
```

## Sintaxe SQL

```sql
CONCAT(<str1>, <str2>[, ...])
```

## Exemplos de SQL

```sql
SELECT CONCAT('Star', 'Rocks');

┌───────────┐
│ StarRocks  │
└───────────┘
```
