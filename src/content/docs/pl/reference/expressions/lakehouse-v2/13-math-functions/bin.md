---
title: BIN (Lakehouse v2)
description: BIN — zwraca binarną reprezentację tekstową liczby całkowitej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/bin.md
---

Zwraca binarną reprezentację tekstową liczby całkowitej.

## Składnia Analyze

```python
func.bin(<x>)
```

## Przykłady Analyze

```python
func.bin(10)

┌────────┐
│ '1010'  │
└────────┘
```

## Składnia SQL

```sql
BIN(<x>)
```

## Przykłady SQL

```sql
SELECT BIN(10);

┌──────┐
│ 1010  │
└──────┘
```
