---
title: LOWER (Lakehouse v2)
description: LOWER — zamienia ciąg na małe litery.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lower.md
---

Zamienia ciąg na małe litery.

## Składnia Analyze

```python
func.lower(<str>)
```

## Przykłady Analyze

```python
func.lower('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Składnia SQL

```sql
LOWER(<str>)
```

## Przykłady SQL

```sql
SELECT LOWER('HELLO');

┌───────┐
│ hello  │
└───────┘
```
