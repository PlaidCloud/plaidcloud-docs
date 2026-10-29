---
title: CHAR_LENGTH (Lakehouse v2)
description: CHAR_LENGTH — gibt die Anzahl der Zeichen in einer Zeichenfolge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/char-length.md
---

Gibt die Anzahl der Zeichen in einer Zeichenfolge zurück.

## Analyze-Syntax

```python
func.char_length(<str>)
```

## Analyze-Beispiele

```python
func.char_length('hello world')

┌────┐
│ 11  │
└────┘
```

## SQL-Syntax

```sql
CHAR_LENGTH(<str>)
```

## SQL-Beispiele

```sql
SELECT CHAR_LENGTH('hello world');

┌────┐
│ 11  │
└────┘
```
