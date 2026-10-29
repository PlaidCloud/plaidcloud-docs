---
title: CHARACTER_LENGTH (Lakehouse v2)
description: CHARACTER_LENGTH — zwraca liczbę znaków w ciągu. Alias funkcji `CHAR_LENGTH`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/character-length.md
---

Zwraca liczbę znaków w ciągu. Alias funkcji `CHAR_LENGTH`.

## Składnia Analyze

```python
func.character_length(<str>)
```

## Przykłady Analyze

```python
func.character_length('hello')

┌───┐
│ 5  │
└───┘
```

## Składnia SQL

```sql
CHARACTER_LENGTH(<str>)
```

## Przykłady SQL

```sql
SELECT CHARACTER_LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
