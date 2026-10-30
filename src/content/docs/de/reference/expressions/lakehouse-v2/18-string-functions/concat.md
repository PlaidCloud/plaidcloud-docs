---
title: CONCAT (Lakehouse v2)
description: CONCAT — verkettet zwei oder mehr Zeichenfolgen.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/concat.md
---

Verkettet zwei oder mehr Zeichenfolgen.

## Analyze-Syntax

```python
func.concat(<str1>, <str2>[, ...])
```

## Analyze-Beispiele

```python
func.concat('Star', 'Rocks')

┌─────────────┐
│ 'StarRocks'  │
└─────────────┘
```

## SQL-Syntax

```sql
CONCAT(<str1>, <str2>[, ...])
```

## SQL-Beispiele

```sql
SELECT CONCAT('Star', 'Rocks');

┌───────────┐
│ StarRocks  │
└───────────┘
```
