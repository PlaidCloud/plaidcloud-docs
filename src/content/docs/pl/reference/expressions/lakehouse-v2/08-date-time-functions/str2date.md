---
title: STR2DATE (Lakehouse v2)
description: STR2DATE — analizuje ciąg znaków do daty przy użyciu ciągu formatu. Alias funkcji `STR_TO_DATE`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/str2date.md
---

Analizuje ciąg znaków do daty przy użyciu ciągu formatu. Alias funkcji `STR_TO_DATE`.

## Składnia Analyze

```python
func.str2date(<str>, <format>)
```

## Przykłady Analyze

```python
func.str2date('2024/06/15', '%Y/%m/%d')

┌──────────────┐
│ '2024-06-15'  │
└──────────────┘
```

## Składnia SQL

```sql
STR2DATE(<str>, <format>)
```

## Przykłady SQL

```sql
SELECT STR2DATE('2024/06/15', '%Y/%m/%d');

┌────────────┐
│ 2024-06-15  │
└────────────┘
```
