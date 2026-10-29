---
title: TO_BASE64 (Lakehouse v1)
description: TO_BASE64 — konwertuje argument tekstowy na postać zakodowaną w base-64 i zwraca wynik jako ciąg znaków.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/to-base64.md
---

Konwertuje argument tekstowy na postać zakodowaną w base-64 i zwraca wynik jako ciąg znaków.
Jeśli argument nie jest ciągiem znaków, przed konwersją jest przekształcany na ciąg.
Wynikiem jest NULL, jeśli argument ma wartość NULL.

## Składnia Analyze

```python
func.to_base64(<v>)
```

## Przykłady Analyze

```python
func.to_base64('abc')
┌───────────────────────┐
│ func.to_base64('abc') │
├───────────────────────┤
│ YWJj                  │
└───────────────────────┘
```

## Składnia SQL

```sql
TO_BASE64(<v>)
```

## Argumenty

| Argumenty | Opis      |
|-----------|-----------|
| `<v>`     | Wartość.  |

## Typ zwracany

`VARCHAR`

## Przykłady SQL

```sql
SELECT TO_BASE64('abc');
┌──────────────────┐
│ TO_BASE64('abc') │
├──────────────────┤
│ YWJj             │
└──────────────────┘
```
