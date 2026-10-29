---
title: FROM_BASE64 (Lakehouse v1)
description: FROM_BASE64 – nimmt eine nach den Base64-Regeln codierte Zeichenfolge entgegen und gibt das decodierte Ergebnis zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/from-base64.md
---

Nimmt eine nach den Base64-Regeln codierte Zeichenfolge entgegen und gibt das decodierte Ergebnis als Binärwert zurück.
Das Ergebnis ist NULL, wenn das Argument NULL oder keine gültige Base64-Zeichenfolge ist.

## Analyze-Syntax

```python
func.from_base64(<expr>)
```

## Analyze-Beispiele

```python
func.from_base64('YWJj')
┌──────────────────────────┐
│ func.from_base64('YWJj') │
├──────────────────────────┤
│ abc                      │
└──────────────────────────┘
```

## SQL-Syntax

```sql
FROM_BASE64(<expr>)
```

## Argumente

| Argumente | Beschreibung          |
|-----------|-----------------------|
| `<expr>`  | Der Zeichenfolgenwert. |

## Rückgabetyp

`BINARY`

## SQL-Beispiele

```sql
SELECT TO_BASE64('abc'), FROM_BASE64(TO_BASE64('abc')) as b, b::String;
┌───────────────────────────────────────┐
│ to_base64('abc') │    b   │ b::string │
│      String      │ Binary │   String  │
├──────────────────┼────────┼───────────┤
│ YWJj             │ 616263 │ abc       │
└───────────────────────────────────────┘
```
