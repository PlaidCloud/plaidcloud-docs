---
title: QUOTE (Lakehouse v1)
description: QUOTE — ujmuje ciąg znaków w cudzysłów, tworząc wynik, którego można użyć jako prawidłowo zabezpieczonej wartości danych w instrukcji SQL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/quote.md
---

Ujmuje ciąg znaków w cudzysłów, tworząc wynik, którego można użyć jako prawidłowo zabezpieczonej wartości danych w instrukcji SQL. 

## Składnia Analyze

```python
func.quote(<str>)
```

## Przykłady Analyze

```python
func.quote('Don\'t')
┌──────────────────────┐
│ func.quote('Don\'t') │
├──────────────────────┤
│  Don\'t!             │
└──────────────────────┘
```

## Składnia SQL

```sql
QUOTE(<str>)
```

## Przykłady SQL

```sql
SELECT QUOTE('Don\'t!');
┌─────────────────┐
│ QUOTE('Don't!') │
├─────────────────┤
│ Don\'t!         │
└─────────────────┘

SELECT QUOTE(NULL);
┌─────────────┐
│ QUOTE(NULL) │
├─────────────┤
│        NULL │
└─────────────┘
```
