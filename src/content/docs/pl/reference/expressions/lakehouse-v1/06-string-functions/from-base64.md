---
title: FROM_BASE64 (Lakehouse v1)
description: FROM_BASE64 — przyjmuje ciąg znaków zakodowany według reguł base-64 i zwraca zdekodowany wynik w postaci binarnej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/from-base64.md
---

Przyjmuje ciąg znaków zakodowany według reguł base-64 i zwraca zdekodowany wynik w postaci binarnej.
Wynikiem jest NULL, jeśli argument ma wartość NULL lub nie jest prawidłowym ciągiem base-64.

## Składnia Analyze

```python
func.from_base64(<expr>)
```

## Przykłady Analyze

```python
func.from_base64('YWJj')
┌──────────────────────────┐
│ func.from_base64('YWJj') │
├──────────────────────────┤
│ abc                      │
└──────────────────────────┘
```

## Składnia SQL

```sql
FROM_BASE64(<expr>)
```

## Argumenty

| Argumenty | Opis                    |
|-----------|-------------------------|
| `<expr>`  | Wartość tekstowa.       |

## Typ zwracany

`BINARY`

## Przykłady SQL

```sql
SELECT TO_BASE64('abc'), FROM_BASE64(TO_BASE64('abc')) as b, b::String;
┌───────────────────────────────────────┐
│ to_base64('abc') │    b   │ b::string │
│      String      │ Binary │   String  │
├──────────────────┼────────┼───────────┤
│ YWJj             │ 616263 │ abc       │
└───────────────────────────────────────┘
```
