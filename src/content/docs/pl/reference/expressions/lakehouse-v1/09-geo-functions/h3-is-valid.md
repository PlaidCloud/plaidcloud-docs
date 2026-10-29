---
title: H3_IS_VALID (Lakehouse v1)
description: H3_IS_VALID — sprawdza, czy podany indeks H3 jest prawidłowy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-valid.md
---

Sprawdza, czy podany indeks [H3](https://eng.uber.com/h3/) jest prawidłowy.

## Składnia Analyze

```python
func.h3_is_valid(h3)
```

## Przykłady Analyze

```python
func.h3_is_valid(644325524701193974)

┌──────────────────────────────────────┐
│ func.h3_is_valid(644325524701193974) │
├──────────────────────────────────────┤
│ true                                 │
└──────────────────────────────────────┘
```

## Składnia SQL

```sql
H3_IS_VALID(h3)
```

## Przykłady SQL

```sql
SELECT H3_IS_VALID(644325524701193974);

┌─────────────────────────────────┐
│ h3_is_valid(644325524701193974) │
├─────────────────────────────────┤
│ true                            │
└─────────────────────────────────┘
```
