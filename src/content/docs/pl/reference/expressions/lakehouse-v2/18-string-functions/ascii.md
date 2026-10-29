---
title: ASCII (Lakehouse v2)
description: ASCII — zwraca kod ASCII pierwszego znaku w ciągu.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ascii.md
---

Zwraca kod ASCII pierwszego znaku w ciągu.

## Składnia Analyze

```python
func.ascii(<str>)
```

## Przykłady Analyze

```python
func.ascii('A')

┌────┐
│ 65  │
└────┘
```

## Składnia SQL

```sql
ASCII(<str>)
```

## Przykłady SQL

```sql
SELECT ASCII('A');

┌────┐
│ 65  │
└────┘
```
