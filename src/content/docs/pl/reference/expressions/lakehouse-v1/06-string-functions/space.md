---
title: SPACE (Lakehouse v1)
description: SPACE — zwraca ciąg znaków składający się z N spacji.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/space.md
---

Zwraca ciąg znaków składający się z N spacji.

## Składnia Analyze

```python
func.space(<n>)
```

## Przykłady Analyze

```python
func.space(20)
┌─────────────────┐
│ func.space(20)  │
├─────────────────┤
│                 │
└─────────────────┘
```

## Składnia SQL

```sql
SPACE(<n>);
```

## Argumenty

| Argumenty | Opis             |
|-----------|------------------|
| `<n>`     | Liczba spacji    |

## Typ zwracany

Wartość typu danych String.

## Przykłady SQL

```sql
SELECT SPACE(20)
┌──────────────────────┐
│ SPACE(20)            │
├──────────────────────┤
│                      │
└──────────────────────┘
```
