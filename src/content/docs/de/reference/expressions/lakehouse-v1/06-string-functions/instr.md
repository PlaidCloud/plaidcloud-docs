---
title: INSTR (Lakehouse v1)
description: INSTR – gibt die Position des ersten Vorkommens der Teilzeichenfolge substr in der Zeichenfolge str zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/instr.md
---

Gibt die Position des ersten Vorkommens der Teilzeichenfolge substr in der Zeichenfolge str zurück.
Das entspricht der Form von LOCATE() mit zwei Argumenten, nur dass die Reihenfolge der Argumente vertauscht ist.

## Analyze-Syntax

```python
func.instr(<str>, <substr>)
```

## Analyze-Beispiele

```python
func.instr('foobarbar', 'bar')
┌────────────────────────────────┐
│ func.instr('foobarbar', 'bar') │
├────────────────────────────────┤
│                              4 │
└────────────────────────────────┘
```

## SQL-Syntax

```sql
INSTR(<str>, <substr>)
```

## Argumente

| Argumente  | Beschreibung           |
|------------|------------------------|
| `<str>`    | Die Zeichenfolge.      |
| `<substr>` | Die Teilzeichenfolge.  |

## Rückgabetyp

`BIGINT`

## SQL-Beispiele

```sql
SELECT INSTR('foobarbar', 'bar');
┌───────────────────────────┐
│ INSTR('foobarbar', 'bar') │
├───────────────────────────┤
│                         4 │
└───────────────────────────┘

SELECT INSTR('xbar', 'foobar');
┌─────────────────────────┐
│ INSTR('xbar', 'foobar') │
├─────────────────────────┤
│                       0 │
└─────────────────────────┘
```
