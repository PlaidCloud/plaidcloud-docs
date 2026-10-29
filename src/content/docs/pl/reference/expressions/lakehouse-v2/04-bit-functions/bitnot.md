---
title: BITNOT (Lakehouse v2)
description: BITNOT — zwraca wynik bitowej operacji NOT na wartości liczbowej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitnot.md
---

Zwraca wynik bitowej operacji NOT na wartości liczbowej.

## Składnia Analyze

```python
func.bitnot(<x>)
```

## Przykłady Analyze

```python
func.bitnot(0)

┌──────┐
│ '-1'  │
└──────┘
```

## Składnia SQL

```sql
BITNOT(<x>)
```

## Przykłady SQL

```sql
SELECT BITNOT(0);

┌────┐
│ -1  │
└────┘
```
