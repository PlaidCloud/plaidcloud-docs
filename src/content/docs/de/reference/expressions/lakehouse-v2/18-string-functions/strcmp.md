---
title: STRCMP (Lakehouse v2)
description: "Verwenden Sie die Zeichenfolgenfunktion STRCMP in PlaidCloud Lakehouse. Vergleicht zwei Zeichenfolgen lexikografisch. Gibt 0 zurück, wenn sie gleich sind, -1, wenn str1 < str2, und 1, wenn str1 > str2."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strcmp.md
---

Vergleicht zwei Zeichenfolgen lexikografisch. Gibt 0 zurück, wenn sie gleich sind, -1, wenn str1 &lt; str2, und 1, wenn str1 > str2.

## Analyze-Syntax

```python
func.strcmp(<str1>, <str2>)
```

## Analyze-Beispiele

```python
func.strcmp('abc', 'abd')

┌────┐
│ -1  │
└────┘
```

## SQL-Syntax

```sql
STRCMP(<str1>, <str2>)
```

## SQL-Beispiele

```sql
SELECT STRCMP('abc', 'abd');

┌────┐
│ -1  │
└────┘
```
