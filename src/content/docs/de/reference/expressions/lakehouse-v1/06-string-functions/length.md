---
title: LENGTH (Lakehouse v1)
description: LENGTH – gibt die Länge einer angegebenen Eingabezeichenfolge oder eines Binärwerts zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/length.md
---

Gibt die Länge einer angegebenen Eingabezeichenfolge oder eines Binärwerts zurück. Bei Zeichenfolgen entspricht die Länge der Anzahl der Zeichen, wobei jedes UTF-8-Zeichen als ein einzelnes Zeichen zählt. Bei Binärdaten entspricht die Länge der Anzahl der Bytes.

## Analyze-Syntax

```python
func.length(<expr>)
```

## Analyze-Beispiele

```python
func.length('Hello')
┌──────────────────────┐
│ func.length('Hello') │
├──────────────────────┤
│                    5 │
└──────────────────────┘
```

## SQL-Syntax

```sql
LENGTH(<expr>)
```

## Aliase

- [CHAR_LENGTH](../char-length)
- [CHARACTER_LENGTH](../character-length)
- [LENGTH_UTF8](../length-utf8)

## Rückgabetyp

BIGINT

## SQL-Beispiele

```sql
SELECT LENGTH('Hello'), LENGTH_UTF8('Hello'), CHAR_LENGTH('Hello'), CHARACTER_LENGTH('Hello');

┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ length('hello') │ length_utf8('hello') │ char_length('hello') │ character_length('hello') │
├─────────────────┼──────────────────────┼──────────────────────┼───────────────────────────┤
│               5 │                    5 │                    5 │                         5 │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```
