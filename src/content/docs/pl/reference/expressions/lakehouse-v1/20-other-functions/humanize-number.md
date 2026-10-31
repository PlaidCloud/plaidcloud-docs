---
title: HUMANIZE_NUMBER (Lakehouse v1)
description: HUMANIZE_NUMBER — zwraca liczbę w postaci czytelnej dla człowieka.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/humanize-number.md
---

Zwraca liczbę w postaci czytelnej dla człowieka.

## Składnia Analyze

```python
func.humanize_number(x);
```

## Przykłady Analyze

```python
func.humanize_number(1000 * 1000)
┌─────────────────────────────────────┐
│ func.humanize_number((1000 * 1000)) │
├─────────────────────────────────────┤
│ 1 million                           │
└─────────────────────────────────────┘
```

## Składnia SQL

```sql
HUMANIZE_NUMBER(x);
```

## Argumenty

| Argumenty | Opis                |
|-----------|----------------------------|
| x         | Rozmiar liczbowy.        |


## Zwracany typ

Ciąg znaków.

## Przykłady SQL

```sql
SELECT HUMANIZE_NUMBER(1000 * 1000)
┌─────────────────────────┐
│ HUMANIZE_NUMBER((1000 * 1000)) │
├─────────────────────────┤
│ 1 million               │
└─────────────────────────┘
```
