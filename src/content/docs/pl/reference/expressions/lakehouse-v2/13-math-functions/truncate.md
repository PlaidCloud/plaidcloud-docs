---
title: TRUNCATE (Lakehouse v2)
description: TRUNCATE — obcina liczbę do określonej liczby miejsc dziesiętnych.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/truncate.md
---

Obcina liczbę do określonej liczby miejsc dziesiętnych.

## Składnia Analyze

```python
func.truncate(<x>, <d>)
```

## Przykłady Analyze

```python
func.truncate(3.14159, 2)

┌──────┐
│ 3.14  │
└──────┘
```

## Składnia SQL

```sql
TRUNCATE(<x>, <d>)
```

## Przykłady SQL

```sql
SELECT TRUNCATE(3.14159, 2);

┌──────┐
│ 3.14  │
└──────┘
```
