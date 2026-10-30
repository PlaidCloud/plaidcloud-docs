---
title: REPEAT (Lakehouse v2)
description: REPEAT — powtarza ciąg podaną liczbę razy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/repeat.md
---

Powtarza ciąg podaną liczbę razy.

## Składnia Analyze

```python
func.repeat(<str>, <n>)
```

## Przykłady Analyze

```python
func.repeat('ab', 3)

┌──────────┐
│ 'ababab'  │
└──────────┘
```

## Składnia SQL

```sql
REPEAT(<str>, <n>)
```

## Przykłady SQL

```sql
SELECT REPEAT('ab', 3);

┌────────┐
│ ababab  │
└────────┘
```
