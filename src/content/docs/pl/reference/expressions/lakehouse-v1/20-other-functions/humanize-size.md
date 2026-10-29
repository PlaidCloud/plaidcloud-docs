---
title: HUMANIZE_SIZE (Lakehouse v1)
description: HUMANIZE_SIZE — zwraca rozmiar w postaci czytelnej dla człowieka, z przyrostkiem (KiB, MiB itd.).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/humanize-size.md
---

Zwraca rozmiar w postaci czytelnej dla człowieka, z przyrostkiem (KiB, MiB itd.).

## Składnia Analyze

```python
func.humanize_size(x);
```

## Przykłady Analyze

```python
func.humanize_size(1024 * 1024)
┌────────────────────────────────────────┐
│ func.func.humanize_size((1024 * 1024)) │
├────────────────────────────────────────┤
│ 1 MiB                                  │
└────────────────────────────────────────┘
```

## Składnia SQL

```sql
HUMANIZE_SIZE(x);
```

## Argumenty

| Argumenty | Opis                |
|-----------|----------------------------|
| x         | Rozmiar liczbowy.        |


## Zwracany typ

Ciąg znaków.

## Przykłady SQL

```sql
SELECT HUMANIZE_SIZE(1024 * 1024)
┌─────────────────────────┐
│ HUMANIZE_SIZE((1024 * 1024)) │
├─────────────────────────┤
│ 1 MiB                    │
└─────────────────────────┘
```
