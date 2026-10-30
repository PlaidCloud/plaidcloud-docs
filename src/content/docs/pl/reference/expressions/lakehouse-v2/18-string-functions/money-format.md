---
title: MONEY_FORMAT (Lakehouse v2)
description: MONEY_FORMAT — formatuje liczbę jako ciąg waluty z przecinkami i dwoma miejscami po przecinku.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/money-format.md
---

Formatuje liczbę jako ciąg waluty z przecinkami i dwoma miejscami po przecinku.

## Składnia Analyze

```python
func.money_format(<num>)
```

## Przykłady Analyze

```python
func.money_format(1234567.89)

┌────────────────┐
│ '1,234,567.89'  │
└────────────────┘
```

## Składnia SQL

```sql
MONEY_FORMAT(<num>)
```

## Przykłady SQL

```sql
SELECT MONEY_FORMAT(1234567.89);

┌──────────────┐
│ 1,234,567.89  │
└──────────────┘
```
