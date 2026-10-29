---
title: STRCMP (Lakehouse v1)
description: STRCMP – gibt 0 zurück, wenn die Zeichenfolgen gleich sind, -1, wenn das erste Argument kleiner als das zweite ist, andernfalls 1.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/strcmp.md
---

Gibt 0 zurück, wenn die Zeichenfolgen gleich sind, -1, wenn das erste Argument kleiner als das zweite ist, andernfalls 1.

## Analyze-Syntax

```python
func.strcmp(<expr1> ,<expr2>)
```

## Analyze-Beispiele

```python
func.strcmp('text', 'text2')
┌──────────────────────────────┐
│ func.strcmp('text', 'text2') │
├──────────────────────────────┤
│                           -1 │
└──────────────────────────────┘

func.strcmp('text2', 'text')
┌──────────────────────────────┐
│ func.strcmp('text2', 'text') │
├──────────────────────────────┤
│                            1 │
└──────────────────────────────┘

func.strcmp('text', 'text')
┌──────────────────────────────┐
│ func.strcmp('text', 'text')  │
├──────────────────────────────┤
│                            0 │
└──────────────────────────────┘
```

## SQL-Syntax

```sql
STRCMP(<expr1> ,<expr2>)
```

## Argumente

| Argumente | Beschreibung      |
|-----------|-------------------|
| `<expr1>` | Die Zeichenfolge. |
| `<expr2>` | Die Zeichenfolge. |

## Rückgabetyp

`BIGINT`

## SQL-Beispiele

```sql
SELECT STRCMP('text', 'text2');
┌─────────────────────────┐
│ STRCMP('text', 'text2') │
├─────────────────────────┤
│                      -1 │
└─────────────────────────┘

SELECT STRCMP('text2', 'text');
┌─────────────────────────┐
│ STRCMP('text2', 'text') │
├─────────────────────────┤
│                       1 │
└─────────────────────────┘

SELECT STRCMP('text', 'text');
┌────────────────────────┐
│ STRCMP('text', 'text') │
├────────────────────────┤
│                      0 │
└────────────────────────┘
```
