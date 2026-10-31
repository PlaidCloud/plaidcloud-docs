---
title: LOCATE (Lakehouse v1)
description: LOCATE – die erste Syntax gibt die Position des ersten Vorkommens der Teilzeichenfolge substr in der Zeichenfolge str zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/locate.md
---

Die erste Syntax gibt die Position des ersten Vorkommens der Teilzeichenfolge substr in der Zeichenfolge str zurück.
Die zweite Syntax gibt die Position des ersten Vorkommens der Teilzeichenfolge substr in der Zeichenfolge str zurück, beginnend bei Position pos.
Gibt 0 zurück, wenn substr nicht in str enthalten ist. Gibt NULL zurück, wenn ein Argument NULL ist.

## Analyze-Syntax

```python
func.locate(<substr>, <str>, <pos>)
```

## Analyze-Beispiele

```python
func.locate('bar', 'foobarbar')
┌────────────────────────────────────┐
│ func.locate('bar', 'foobarbar') │
├────────────────────────────────────┤
│                                  5 │
└────────────────────────────────────┘
```

```python
func.locate('bar', 'foobarbar', 5)
┌────────────────────────────────────┐
│ func.locate('bar', 'foobarbar', 5) │
├────────────────────────────────────┤
│                                  7 │
└────────────────────────────────────┘
```

## SQL-Syntax

```sql
LOCATE(<substr>, <str>)
LOCATE(<substr>, <str>, <pos>)
```

## Argumente

| Argumente  | Beschreibung          |
|------------|-----------------------|
| `<substr>` | Die Teilzeichenfolge. |
| `<str>`    | Die Zeichenfolge.     |
| `<pos>`    | Die Position.         |

## Rückgabetyp

`BIGINT`

## SQL-Beispiele

```sql
SELECT LOCATE('bar', 'foobarbar')
┌────────────────────────────┐
│ LOCATE('bar', 'foobarbar') │
├────────────────────────────┤
│                          4 │
└────────────────────────────┘

SELECT LOCATE('xbar', 'foobar')
┌──────────────────────────┐
│ LOCATE('xbar', 'foobar') │
├──────────────────────────┤
│                        0 │
└──────────────────────────┘

SELECT LOCATE('bar', 'foobarbar', 5)
┌───────────────────────────────┐
│ LOCATE('bar', 'foobarbar', 5) │
├───────────────────────────────┤
│                             7 │
└───────────────────────────────┘
```
