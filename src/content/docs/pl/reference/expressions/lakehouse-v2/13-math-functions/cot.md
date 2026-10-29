---
title: COT (Lakehouse v2)
description: COT — zwraca cotangens liczby w radianach.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cot.md
---

Zwraca cotangens liczby w radianach.

## Składnia Analyze

```python
func.cot(<x>)
```

## Przykłady Analyze

```python
func.cot(1)

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```

## Składnia SQL

```sql
COT(<x>)
```

## Przykłady SQL

```sql
SELECT COT(1);

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```
