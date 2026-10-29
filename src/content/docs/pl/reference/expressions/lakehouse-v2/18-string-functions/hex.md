---
title: HEX (Lakehouse v2)
description: HEX — zwraca reprezentację szesnastkową ciągu lub liczby.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/hex.md
---

Zwraca reprezentację szesnastkową ciągu lub liczby.

## Składnia Analyze

```python
func.hex(<expr>)
```

## Przykłady Analyze

```python
func.hex(255)

┌──────┐
│ 'FF'  │
└──────┘
```

## Składnia SQL

```sql
HEX(<expr>)
```

## Przykłady SQL

```sql
SELECT HEX(255);

┌────┐
│ FF  │
└────┘
```
