---
title: BIN (Lakehouse v1)
description: BIN — zwraca tekstową reprezentację wartości binarnej liczby N.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/bin.md
---

Zwraca tekstową reprezentację wartości binarnej liczby N.

## Składnia Analyze

```python
func.bin(<expr>)
```

## Przykłady Analyze

```python
func.bin(12)
┌──────────────┐
│ func.bin(12) │
├──────────────┤
│ 1100         │
└──────────────┘
```

## Składnia SQL

```sql
BIN(<expr>)
```

## Argumenty

| Argumenty | Opis    |
|-----------|---------|
| `<expr>`  | Liczba. |

## Typ zwracany

`VARCHAR`

## Przykłady SQL

```sql
SELECT BIN(12);
┌─────────┐
│ BIN(12) │
├─────────┤
│ 1100    │
└─────────┘
```
