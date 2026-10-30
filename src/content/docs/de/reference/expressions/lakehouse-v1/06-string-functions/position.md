---
title: POSITION (Lakehouse v1)
description: POSITION – POSITION(substr IN str) ist ein Synonym für LOCATE(substr,str).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/position.md
---

POSITION(substr IN str) ist ein Synonym für LOCATE(substr,str).
Gibt die Position des ersten Vorkommens der Teilzeichenfolge substr in der Zeichenfolge str zurück.
Gibt 0 zurück, wenn substr nicht in str enthalten ist. Gibt NULL zurück, wenn ein Argument NULL ist.

## Analyze-Syntax

```python
func.position(<substr>, <str>)
```

## Analyze-Beispiele

```python
func.position('bar', 'foobarbar')
┌───────────────────────────────────┐
│ func.position('bar', 'foobarbar') │
├───────────────────────────────────┤
│                                 4 │
└───────────────────────────────────┘
```

## SQL-Syntax

```sql
POSITION(<substr> IN <str>)
```

## Argumente

| Argumente  | Beschreibung          |
|------------|-----------------------|
| `<substr>` | Die Teilzeichenfolge. |
| `<str>`    | Die Zeichenfolge.     |

## Rückgabetyp

`BIGINT`

## SQL-Beispiele

```sql
SELECT POSITION('bar' IN 'foobarbar')
┌────────────────────────────┐
│ POSITION('bar' IN 'foobarbar') │
├────────────────────────────┤
│                          4 │
└────────────────────────────┘

SELECT POSITION('xbar' IN 'foobar')
┌──────────────────────────┐
│ POSITION('xbar' IN 'foobar') │
├──────────────────────────┤
│                        0 │
└──────────────────────────┘
```
