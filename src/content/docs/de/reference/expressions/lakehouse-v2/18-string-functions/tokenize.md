---
title: TOKENIZE (Lakehouse v2)
description: "Verwenden Sie die Zeichenfolgenfunktion TOKENIZE in PlaidCloud Lakehouse. Zerlegt eine Zeichenfolge mit dem angegebenen Analyzer in ein Array von Begriffen. Nützlich für die Volltextsuche."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/tokenize.md
---

Zerlegt eine Zeichenfolge mit dem angegebenen Analyzer in ein Array von Begriffen. Nützlich für Szenarien der Volltextsuche.

## Analyze-Syntax

```python
func.tokenize('The quick brown fox', 'english')
```

## Analyze-Beispiele

```python
func.tokenize('The quick brown fox', 'english')

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```

## SQL-Syntax

```sql
TOKENIZE(<str>[, <analyzer>])
```

## SQL-Beispiele

```sql
SELECT TOKENIZE('The quick brown fox', 'english');

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```
