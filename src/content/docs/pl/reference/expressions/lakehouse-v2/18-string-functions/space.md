---
title: SPACE (Lakehouse v2)
description: SPACE — zwraca ciąg składający się z podanej liczby spacji.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/space.md
---

Zwraca ciąg składający się z podanej liczby spacji.

## Składnia Analyze

```python
func.space(<n>)
```

## Przykłady Analyze

```python
func.space(5)

┌─────────┐
│ '     '  │
└─────────┘
```

## Składnia SQL

```sql
SPACE(<n>)
```

## Przykłady SQL

```sql
SELECT CONCAT('>', SPACE(5), '<');

┌─────────┐
│ >     <  │
└─────────┘
```
