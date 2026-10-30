---
title: UNHEX (Lakehouse v1)
description: UNHEX – für ein Zeichenfolgenargument str interpretiert UNHEX(str) jedes Zeichenpaar im Argument.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/unhex.md
---

Für ein Zeichenfolgenargument str interpretiert UNHEX(str) jedes Zeichenpaar im Argument als Hexadezimalzahl und konvertiert es in das durch die Zahl dargestellte Byte. Der Rückgabewert ist eine binäre Zeichenfolge.

## Analyze-Syntax

```python
func.unhex(<expr>)
```

## Analyze-Beispiele

```python
func.unhex('6461746162656e64')
┌────────────────────────────────┐
│ func.unhex('6461746162656e64') │
├────────────────────────────────┤
│ 6461746162656E64               │
└────────────────────────────────┘
```

## SQL-Syntax

```sql
UNHEX(<expr>)
```

## Aliasse

- [FROM_HEX](../from-hex)

## SQL-Beispiele

```sql
SELECT UNHEX('6461746162656e64') as c1, typeof(c1),UNHEX('6461746162656e64')::varchar as c2, typeof(c2), FROM_HEX('6461746162656e64');

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│           c1              │     typeof(c1)         │       c2         |    typeof(c2)     |   from_hex('6461746162656e64')  |
├───────────────────────────┼────────────────────────|──────────────────┤───────────────────|─────────────────────────────────┤
│ 6461746162656E64          │      binary            │      databend    |    varchar        |   6461746162656E64              |
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT UNHEX(HEX('string')), unhex(HEX('string'))::varchar;

┌──────────────────────────────────────────────────────┐
│ unhex(hex('string')) │ unhex(hex('string'))::varchar │
├──────────────────────┼───────────────────────────────┤
│ 737472696E67         │ string                        │
└──────────────────────────────────────────────────────┘
```
