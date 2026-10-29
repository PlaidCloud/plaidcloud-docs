---
title: STRLEFT (Lakehouse v2)
description: STRLEFT — zwraca N pierwszych znaków od lewej strony ciągu. Alias funkcji `LEFT`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strleft.md
---

Zwraca N pierwszych znaków od lewej strony ciągu. Alias funkcji `LEFT`.

## Składnia Analyze

```python
func.strleft(<str>, <len>)
```

## Przykłady Analyze

```python
func.strleft('StarRocks', 4)

┌────────┐
│ 'Star'  │
└────────┘
```

## Składnia SQL

```sql
STRLEFT(<str>, <len>)
```

## Przykłady SQL

```sql
SELECT STRLEFT('StarRocks', 4);

┌──────┐
│ Star  │
└──────┘
```
