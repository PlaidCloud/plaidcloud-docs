---
title: REVERSE (Lakehouse v1)
description: REVERSE — zwraca ciąg znaków str z odwróconą kolejnością znaków.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/reverse.md
---

Zwraca ciąg znaków str z odwróconą kolejnością znaków.

## Składnia Analyze

```python
func.reverse(<str>)
```

## Przykłady Analyze

```python
func.reverse('abc')
┌──────────────────────┐
│ func..reverse('abc') │
├──────────────────────┤
│ cba                  │
└──────────────────────┘
```

## Składnia SQL

```sql
REVERSE(<str>)
```

## Argumenty

| Argumenty | Opis               |
|-----------|--------------------|
| `<str>`   | Wartość tekstowa.  |

## Typ zwracany

`VARCHAR`

## Przykłady SQL

```sql
SELECT REVERSE('abc');
┌────────────────┐
│ REVERSE('abc') │
├────────────────┤
│ cba            │
└────────────────┘
```
