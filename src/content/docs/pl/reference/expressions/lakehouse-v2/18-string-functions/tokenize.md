---
title: TOKENIZE (Lakehouse v2)
description: "Użyj funkcji tekstowej TOKENIZE w PlaidCloud Lakehouse. Dzieli ciąg na tablicę terminów za pomocą wskazanego analizatora. Przydatna w wyszukiwaniu pełnotekstowym."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/tokenize.md
---

Dzieli ciąg na tablicę terminów za pomocą wskazanego analizatora. Przydatna w scenariuszach wyszukiwania pełnotekstowego.

## Składnia Analyze

```python
func.tokenize('The quick brown fox', 'english')
```

## Przykłady Analyze

```python
func.tokenize('The quick brown fox', 'english')

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```

## Składnia SQL

```sql
TOKENIZE(<str>[, <analyzer>])
```

## Przykłady SQL

```sql
SELECT TOKENIZE('The quick brown fox', 'english');

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```
