---
title: REPEAT (Lakehouse v1)
description: REPEAT — zwraca ciąg znaków składający się z ciągu str powtórzonego count razy.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/repeat.md
---

Zwraca ciąg znaków składający się z ciągu str powtórzonego count razy. Jeśli count jest mniejsze niż 1, zwraca pusty ciąg. Zwraca NULL, jeśli str lub count ma wartość NULL.

## Składnia Analyze

```python
func.repeat(<str>, <count>)
```

## Przykłady Analyze

```python
func.repeat(<str>, <count>)
┌─────────────────────────┐
│ func.repeat('plaid', 3) │
├─────────────────────────┤
│ plaidplaidplaid         │
└─────────────────────────┘
```

## Składnia SQL

```sql
REPEAT(<str>, <count>)
```

## Argumenty

| Argumenty | Opis         |
|-----------|--------------|
| `<str>`   | Ciąg znaków. |
| `<count>` | Liczba.      |

## Przykłady SQL

```sql
SELECT REPEAT('databend', 3);
┌──────────────────────────┐
│ REPEAT('databend', 3)    │
├──────────────────────────┤
│ databenddatabenddatabend │
└──────────────────────────┘

SELECT REPEAT('databend', 0);
┌───────────────────────┐
│ REPEAT('databend', 0) │
├───────────────────────┤
│                       │
└───────────────────────┘

SELECT REPEAT('databend', NULL);
┌──────────────────────────┐
│ REPEAT('databend', NULL) │
├──────────────────────────┤
│                     NULL │
└──────────────────────────┘
```
