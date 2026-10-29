---
title: REGEXP_EXTRACT (Lakehouse v2)
description: REGEXP_EXTRACT — wyodrębnia pierwszy podciąg pasujący do wzorca wyrażenia regularnego.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-extract.md
---

Wyodrębnia pierwszy podciąg pasujący do wzorca wyrażenia regularnego.

## Składnia Analyze

```python
func.regexp_extract(<str>, <pattern>[, <group>])
```

## Przykłady Analyze

```python
func.regexp_extract('price: $42.50', '\\$(\\d+\\.\\d+)', 1)

┌─────────┐
│ '42.50'  │
└─────────┘
```

## Składnia SQL

```sql
REGEXP_EXTRACT(<str>, <pattern>[, <group>])
```

## Przykłady SQL

```sql
SELECT REGEXP_EXTRACT('price: $42.50', '\\$(\\d+\\.\\d+)', 1);

┌───────┐
│ 42.50  │
└───────┘
```
