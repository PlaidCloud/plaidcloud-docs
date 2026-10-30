---
title: LEFT (Lakehouse v1)
description: LEFT – gibt die ganz links stehenden len Zeichen der Zeichenfolge str zurück, oder NULL, wenn ein Argument NULL ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/left.md
---

Gibt die ganz links stehenden len Zeichen der Zeichenfolge str zurück, oder NULL, wenn ein Argument NULL ist.

## Analyze-Syntax

```python
func.left(<str>, <len>)
```

## Analyze-Beispiele

```python
func.left('foobarbar', 5)
┌───────────────────────────┐
│ func.left('foobarbar', 5) │
├───────────────────────────┤
│ fooba                     │
└───────────────────────────┘
```

## SQL-Syntax

```sql
LEFT(<str>, <len>);
```

## Argumente

| Argumente | Beschreibung                                                     |
|-----------|------------------------------------------------------------------|
| `<str>`   | Die Hauptzeichenfolge, aus der die Zeichen extrahiert werden     |
| `<len>`   | Die Anzahl der Zeichen                                           |

## Rückgabetyp

`VARCHAR`

## SQL-Beispiele

```sql
SELECT LEFT('foobarbar', 5);
┌──────────────────────┐
│ LEFT('foobarbar', 5) │
├──────────────────────┤
│ fooba                │
└──────────────────────┘
```
