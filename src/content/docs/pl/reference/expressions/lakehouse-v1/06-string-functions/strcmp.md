---
title: STRCMP (Lakehouse v1)
description: STRCMP — zwraca 0, jeśli ciągi znaków są takie same, -1, jeśli pierwszy argument jest mniejszy od drugiego, a w pozostałych przypadkach 1.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/strcmp.md
---

Zwraca 0, jeśli ciągi znaków są takie same, -1, jeśli pierwszy argument jest mniejszy od drugiego, a w pozostałych przypadkach 1.

## Składnia Analyze

```python
func.strcmp(<expr1> ,<expr2>)
```

## Przykłady Analyze

```python
func.strcmp('text', 'text2')
┌──────────────────────────────┐
│ func.strcmp('text', 'text2') │
├──────────────────────────────┤
│                           -1 │
└──────────────────────────────┘

func.strcmp('text2', 'text')
┌──────────────────────────────┐
│ func.strcmp('text2', 'text') │
├──────────────────────────────┤
│                            1 │
└──────────────────────────────┘

func.strcmp('text', 'text')
┌──────────────────────────────┐
│ func.strcmp('text', 'text')  │
├──────────────────────────────┤
│                            0 │
└──────────────────────────────┘
```

## Składnia SQL

```sql
STRCMP(<expr1> ,<expr2>)
```

## Argumenty

| Argumenty | Opis         |
|-----------|--------------|
| `<expr1>` | Ciąg znaków. |
| `<expr2>` | Ciąg znaków. |

## Typ zwracany

`BIGINT`

## Przykłady SQL

```sql
SELECT STRCMP('text', 'text2');
┌─────────────────────────┐
│ STRCMP('text', 'text2') │
├─────────────────────────┤
│                      -1 │
└─────────────────────────┘

SELECT STRCMP('text2', 'text');
┌─────────────────────────┐
│ STRCMP('text2', 'text') │
├─────────────────────────┤
│                       1 │
└─────────────────────────┘

SELECT STRCMP('text', 'text');
┌────────────────────────┐
│ STRCMP('text', 'text') │
├────────────────────────┤
│                      0 │
└────────────────────────┘
```
