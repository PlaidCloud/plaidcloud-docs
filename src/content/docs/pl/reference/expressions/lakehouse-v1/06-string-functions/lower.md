---
title: LOWER (Lakehouse v1)
description: LOWER — zwraca ciąg znaków, w którym wszystkie znaki zamieniono na małe litery.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/lower.md
---

Zwraca ciąg znaków, w którym wszystkie znaki zamieniono na małe litery.

## Składnia Analyze

```python
func.lower(<str>)
```

## Przykłady Analyze

```python
func.lower('Hello, PlaidCloud!')
┌──────────────────────────────────┐
│ func.lower('Hello, PlaidCloud!') │
├──────────────────────────────────┤
│ hello, plaidcloud!               │
└──────────────────────────────────┘
```

## Składnia SQL

```sql
LOWER(<str>)
```

## Aliasy

- [LCASE](../lcase)

## Typ zwracany

VARCHAR

## Przykłady SQL

```sql
SELECT LOWER('Hello, Databend!'), LCASE('Hello, Databend!');

┌───────────────────────────────────────────────────────┐
│ lower('hello, databend!') │ lcase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ hello, databend!          │ hello, databend!          │
└───────────────────────────────────────────────────────┘
```
