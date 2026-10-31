---
title: SPACE (Lakehouse v1)
description: SPACE – gibt eine Zeichenfolge aus N Leerzeichen zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/space.md
---

Gibt eine Zeichenfolge aus N Leerzeichen zurück.

## Analyze-Syntax

```python
func.space(<n>)
```

## Analyze-Beispiele

```python
func.space(20)
┌─────────────────┐
│ func.space(20)  │
├─────────────────┤
│                 │
└─────────────────┘
```

## SQL-Syntax

```sql
SPACE(<n>);
```

## Argumente

| Argumente | Beschreibung           |
|-----------|------------------------|
| `<n>`     | Die Anzahl der Leerzeichen |

## Rückgabetyp

Wert vom Datentyp Zeichenfolge.

## SQL-Beispiele

```sql
SELECT SPACE(20)
┌──────────────────────┐
│ SPACE(20)            │
├──────────────────────┤
│                      │
└──────────────────────┘
```
