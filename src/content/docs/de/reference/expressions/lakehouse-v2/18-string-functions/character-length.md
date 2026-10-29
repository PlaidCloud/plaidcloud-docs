---
title: CHARACTER_LENGTH (Lakehouse v2)
description: CHARACTER_LENGTH — gibt die Anzahl der Zeichen in einer Zeichenfolge zurück. Alias für `CHAR_LENGTH`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/character-length.md
---

Gibt die Anzahl der Zeichen in einer Zeichenfolge zurück. Alias für `CHAR_LENGTH`.

## Analyze-Syntax

```python
func.character_length(<str>)
```

## Analyze-Beispiele

```python
func.character_length('hello')

┌───┐
│ 5  │
└───┘
```

## SQL-Syntax

```sql
CHARACTER_LENGTH(<str>)
```

## SQL-Beispiele

```sql
SELECT CHARACTER_LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
