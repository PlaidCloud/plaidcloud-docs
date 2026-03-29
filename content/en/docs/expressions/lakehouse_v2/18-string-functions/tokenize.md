---
title: TOKENIZE
---

Tokenizes a string into an array of terms using the specified analyzer. Useful for full-text search scenarios.

## Analyze Syntax

```python
func.tokenize('The quick brown fox', 'english')
```

## Analyze Examples

```python
func.tokenize('The quick brown fox', 'english')

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```

## SQL Syntax

```sql
TOKENIZE(<str>[, <analyzer>])
```

## SQL Examples

```sql
SELECT TOKENIZE('The quick brown fox', 'english');

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```
