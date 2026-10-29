---
title: UPPER (Lakehouse v2)
description: UPPER — zamienia ciąg na wielkie litery.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/upper.md
---

Zamienia ciąg na wielkie litery.

## Składnia Analyze

```python
func.upper(<str>)
```

## Przykłady Analyze

```python
func.upper('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## Składnia SQL

```sql
UPPER(<str>)
```

## Przykłady SQL

```sql
SELECT UPPER('hello');

┌───────┐
│ HELLO  │
└───────┘
```
