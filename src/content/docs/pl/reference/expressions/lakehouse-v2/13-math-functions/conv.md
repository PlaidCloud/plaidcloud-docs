---
title: CONV (Lakehouse v2)
description: CONV — konwertuje liczbę z jednego systemu liczbowego na inny.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/conv.md
---

Konwertuje liczbę z jednego systemu liczbowego na inny.

## Składnia Analyze

```python
func.conv(<num>, <from_base>, <to_base>)
```

## Przykłady Analyze

```python
func.conv('ff', 16, 10)

┌───────┐
│ '255'  │
└───────┘
```

## Składnia SQL

```sql
CONV(<num>, <from_base>, <to_base>)
```

## Przykłady SQL

```sql
SELECT CONV('ff', 16, 10);

┌─────┐
│ 255  │
└─────┘
```
