---
title: SUBSTRING_INDEX (Lakehouse v2)
description: "Użyj funkcji tekstowej SUBSTRING_INDEX w PlaidCloud Lakehouse. Zwraca podciąg znajdujący się przed lub po podanej liczbie wystąpień ogranicznika."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substring-index.md
---

Zwraca podciąg znajdujący się przed lub po podanej liczbie wystąpień ogranicznika.

## Składnia Analyze

```python
func.substring_index(<str>, <delim>, <count>)
```

## Przykłady Analyze

```python
func.substring_index('www.example.com', '.', 2)

┌───────────────┐
│ 'www.example'  │
└───────────────┘
```

## Składnia SQL

```sql
SUBSTRING_INDEX(<str>, <delim>, <count>)
```

## Przykłady SQL

```sql
SELECT SUBSTRING_INDEX('www.example.com', '.', 2);

┌─────────────┐
│ www.example  │
└─────────────┘
```
