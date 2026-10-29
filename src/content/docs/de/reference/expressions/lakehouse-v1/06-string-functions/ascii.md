---
title: ASCII (Lakehouse v1)
description: ASCII – gibt den numerischen Wert des ganz links stehenden Zeichens der Zeichenfolge str zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ascii.md
---

Gibt den numerischen Wert des ganz links stehenden Zeichens der Zeichenfolge str zurück.

## Analyze-Syntax

```python
func.ascii(<expr>)
```

## Analyze-Beispiele

```python
func.ascii('2')
┌─────────────────┐
│ func.ascii('2') │
├─────────────────┤
│              50 │
└─────────────────┘
```

## SQL-Syntax

```sql
ASCII(<expr>)
```

## Argumente

| Argumente | Beschreibung      |
|-----------|-------------------|
| `<expr>`  | Die Zeichenfolge. |

## Rückgabetyp

`TINYINT`

## SQL-Beispiele

```sql
SELECT ASCII('2');
┌────────────┐
│ ASCII('2') │
├────────────┤
│         50 │
└────────────┘
```
