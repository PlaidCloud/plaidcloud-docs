---
title: ENDS_WITH (Lakehouse v2)
description: ENDS_WITH — sprawdza, czy ciąg kończy się podanym sufiksem.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ends-with.md
---

Sprawdza, czy ciąg kończy się podanym sufiksem.

## Składnia Analyze

```python
func.ends_with(<str>, <suffix>)
```

## Przykłady Analyze

```python
func.ends_with('hello world', 'world')

┌───┐
│ 1  │
└───┘
```

## Składnia SQL

```sql
ENDS_WITH(<str>, <suffix>)
```

## Przykłady SQL

```sql
SELECT ENDS_WITH('hello world', 'world');

┌───┐
│ 1  │
└───┘
```
