---
title: APPEND_TRAILING_CHAR_IF_ABSENT (Lakehouse v2)
description: "Verwenden Sie die Zeichenfolgenfunktion APPEND_TRAILING_CHAR_IF_ABSENT in PlaidCloud Lakehouse. Hängt ein abschließendes Zeichen an eine Zeichenfolge an, wenn es noch nicht vorhanden ist."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/append-trailing-char-if-absent.md
---

Hängt ein abschließendes Zeichen an eine Zeichenfolge an, wenn es noch nicht vorhanden ist.

## Analyze-Syntax

```python
func.append_trailing_char_if_absent(<str>, <char>)
```

## Analyze-Beispiele

```python
func.append_trailing_char_if_absent('hello', '!')

┌──────────┐
│ 'hello!'  │
└──────────┘
```

## SQL-Syntax

```sql
APPEND_TRAILING_CHAR_IF_ABSENT(<str>, <char>)
```

## SQL-Beispiele

```sql
SELECT APPEND_TRAILING_CHAR_IF_ABSENT('hello', '!');

┌────────┐
│ hello!  │
└────────┘
```
