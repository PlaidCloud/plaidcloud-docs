---
title: BITOR (Lakehouse v2)
description: BITOR — zwraca wynik bitowej operacji OR na dwóch wartościach liczbowych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitor.md
---

Zwraca wynik bitowej operacji OR na dwóch wartościach liczbowych.

## Składnia Analyze

```python
func.bitor(<x>, <y>)
```

## Przykłady Analyze

```python
func.bitor(12, 10)

┌────┐
│ 14  │
└────┘
```

## Składnia SQL

```sql
BITOR(<x>, <y>)
```

## Przykłady SQL

```sql
SELECT BITOR(12, 10);

┌────┐
│ 14  │
└────┘
```
