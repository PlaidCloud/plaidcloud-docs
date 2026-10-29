---
title: RIGHT (Lakehouse v1)
description: RIGHT – gibt die ganz rechts stehenden len Zeichen der Zeichenfolge str zurück, oder NULL, wenn ein Argument NULL ist.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/right.md
---

Gibt die ganz rechts stehenden len Zeichen der Zeichenfolge str zurück, oder NULL, wenn ein Argument NULL ist.

## Analyze-Syntax

```python
func.right(<str>, <len>)
```

## Analyze-Beispiele

```python
func.right('foobarbar', 4)
┌────────────────────────────┐
│ func.right('foobarbar', 4) │
├────────────────────────────┤
│ rbar                       │
└────────────────────────────┘
```

## SQL-Syntax

```sql
RIGHT(<str>, <len>);
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
SELECT RIGHT('foobarbar', 4);
┌───────────────────────┐
│ RIGHT('foobarbar', 4) │
├───────────────────────┤
│ rbar                  │
└───────────────────────┘
```
