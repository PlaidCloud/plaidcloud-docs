---
title: SUBSTRING (Lakehouse v2)
description: SUBSTRING — zwraca podciąg zaczynający się od podanej pozycji. Alias funkcji `SUBSTR`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substring.md
---

Zwraca podciąg zaczynający się od podanej pozycji. Alias funkcji `SUBSTR`.

## Składnia Analyze

```python
func.substring(<str>, <pos>[, <len>])
```

## Przykłady Analyze

```python
func.substring('StarRocks', 1, 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## Składnia SQL

```sql
SUBSTRING(<str>, <pos>[, <len>])
```

## Przykłady SQL

```sql
SELECT SUBSTRING('StarRocks', 1, 4);

┌──────┐
│ Star  │
└──────┘
```
