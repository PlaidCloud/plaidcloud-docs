---
title: TO_BASE64 (Lakehouse v1)
description: TO_BASE64 – wandelt das Zeichenfolgenargument in die Base64-codierte Form um und gibt das Ergebnis als Zeichenfolge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/to-base64.md
---

Wandelt das Zeichenfolgenargument in die Base64-codierte Form um und gibt das Ergebnis als Zeichenfolge zurück.
Ist das Argument keine Zeichenfolge, wird es vor der Umwandlung in eine Zeichenfolge konvertiert.
Das Ergebnis ist NULL, wenn das Argument NULL ist.

## Analyze-Syntax

```python
func.to_base64(<v>)
```

## Analyze-Beispiele

```python
func.to_base64('abc')
┌───────────────────────┐
│ func.to_base64('abc') │
├───────────────────────┤
│ YWJj                  │
└───────────────────────┘
```

## SQL-Syntax

```sql
TO_BASE64(<v>)
```

## Argumente

| Argumente | Beschreibung |
|-----------|--------------|
| `<v>`     | Der Wert.    |

## Rückgabetyp

`VARCHAR`

## SQL-Beispiele

```sql
SELECT TO_BASE64('abc');
┌──────────────────┐
│ TO_BASE64('abc') │
├──────────────────┤
│ YWJj             │
└──────────────────┘
```
