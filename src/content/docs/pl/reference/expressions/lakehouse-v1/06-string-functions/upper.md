---
title: UPPER (Lakehouse v1)
description: UPPER — zwraca ciąg znaków, w którym wszystkie znaki zmieniono na wielkie litery.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/upper.md
---

Zwraca ciąg znaków, w którym wszystkie znaki zmieniono na wielkie litery.

## Składnia Analyze

```python
func.unhex(<expr>)
```

## Przykłady Analyze

```python
func.upper('hello, plaidcloud lakehouse!')
┌────────────────────────────────────────────┐
│ func.upper('hello, plaidcloud lakehouse!') │
├────────────────────────────────────────────┤
│ 'HELLO, PLAIDCLOUD LAKEHOUSE!'             │
└────────────────────────────────────────────┘
```

## Składnia SQL

```sql
UPPER(<str>)
```

## Aliasy

- [UCASE](../ucase)

## Typ zwracany

VARCHAR

## Przykłady SQL

```sql
SELECT UPPER('hello, databend!'), UCASE('hello, databend!');

┌───────────────────────────────────────────────────────┐
│ upper('hello, databend!') │ ucase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ HELLO, DATABEND!          │ HELLO, DATABEND!          │
└───────────────────────────────────────────────────────┘
```
