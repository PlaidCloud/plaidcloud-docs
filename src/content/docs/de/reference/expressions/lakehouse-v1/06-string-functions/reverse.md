---
title: REVERSE (Lakehouse v1)
description: REVERSE – gibt die Zeichenfolge str mit umgekehrter Zeichenreihenfolge zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/reverse.md
---

Gibt die Zeichenfolge str mit umgekehrter Zeichenreihenfolge zurück.

## Analyze-Syntax

```python
func.reverse(<str>)
```

## Analyze-Beispiele

```python
func.reverse('abc')
┌──────────────────────┐
│ func..reverse('abc') │
├──────────────────────┤
│ cba                  │
└──────────────────────┘
```

## SQL-Syntax

```sql
REVERSE(<str>)
```

## Argumente

| Argumente | Beschreibung              |
|-----------|---------------------------|
| `<str>`   | Der Zeichenfolgenwert.    |

## Rückgabetyp

`VARCHAR`

## SQL-Beispiele

```sql
SELECT REVERSE('abc');
┌────────────────┐
│ REVERSE('abc') │
├────────────────┤
│ cba            │
└────────────────┘
```
