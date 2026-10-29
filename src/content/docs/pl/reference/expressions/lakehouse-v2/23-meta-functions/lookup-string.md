---
title: LOOKUP_STRING (Lakehouse v2)
description: LOOKUP_STRING — wyszukuje ciąg w słowniku i zwraca odpowiadający mu identyfikator.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/lookup-string.md
---

Wyszukuje ciąg w słowniku i zwraca odpowiadający mu identyfikator.

## Składnia Analyze

```python
func.lookup_string(<dict_table>, <value>)
```

## Przykłady Analyze

```python
func.lookup_string('status_dict', 'Active')

┌───┐
│ 1  │
└───┘
```

## Składnia SQL

```sql
LOOKUP_STRING(<dict_table>, <value>)
```

## Przykłady SQL

```sql
SELECT LOOKUP_STRING('status_dict', 'Active');

┌───┐
│ 1  │
└───┘
```
