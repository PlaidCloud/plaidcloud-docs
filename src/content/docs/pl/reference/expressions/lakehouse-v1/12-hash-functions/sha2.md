---
title: SHA2 (Lakehouse v1)
description: SHA2 — oblicza skróty z rodziny funkcji SHA-2 (SHA-224, SHA-256, SHA-384 i SHA-512).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/12-hash-functions/sha2.md
---

Oblicza skróty z rodziny funkcji SHA-2 (SHA-224, SHA-256, SHA-384 i SHA-512). Jeśli długość skrótu nie jest jedną z dozwolonych wartości, zwracana jest wartość NULL. W przeciwnym razie wynikiem funkcji jest wartość skrótu o żądanej liczbie bitów, zapisana jako ciąg cyfr szesnastkowych.

## Składnia Analyze

```python
func.sha2(<expr>, <expr>)
```

## Przykłady Analyze

```python
func.sha2('1234567890', 0)

┌──────────────────────────────────────────────────────────────────┐
│ func.sha2('1234567890', 0))                                      │
├──────────────────────────────────────────────────────────────────┤
│ c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646 │
└──────────────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
SHA2(<expr>, <expr>)
```

## Przykłady SQL

```sql
SELECT SHA2('1234567890', 0);

┌──────────────────────────────────────────────────────────────────┐
│                       sha2('1234567890', 0)                      │
├──────────────────────────────────────────────────────────────────┤
│ c775e7b757ede630cd0aa1113bd102661ab38829ca52a6422ab782862f268646 │
└──────────────────────────────────────────────────────────────────┘
```
