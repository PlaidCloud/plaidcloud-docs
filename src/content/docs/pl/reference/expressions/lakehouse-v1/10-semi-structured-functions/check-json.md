---
title: CHECK_JSON (Lakehouse v1)
description: CHECK_JSON — sprawdza poprawność dokumentu JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/check-json.md
---

Sprawdza poprawność dokumentu JSON.
Jeśli ciąg wejściowy jest prawidłowym dokumentem JSON lub wartością `NULL`, wynikiem jest `NULL`.
Jeśli ciągu wejściowego nie można przekształcić w prawidłową wartość JSON, ciąg wynikowy zawiera komunikat o błędzie.

## Składnia Analyze

```python
func.check_json(<expr>)
```

## Przykłady Analyze

```python
func.check_json('[1,2,3]');
┌────────────────────────────┐
│ func.check_json('[1,2,3]') │
├────────────────────────────┤
│ NULL                       │
└────────────────────────────┘
```

## Składnia SQL

```sql
CHECK_JSON( <expr> )
```

## Argumenty

| Argumenty | Opis                         |
|-----------|------------------------------|
| `<expr>`  | Wyrażenie typu ciągu znaków  |

## Typ zwracany

String

## Przykłady SQL

```sql
SELECT check_json('[1,2,3]');
┌───────────────────────┐
│ check_json('[1,2,3]') │
├───────────────────────┤
│ NULL                  │
└───────────────────────┘

SELECT check_json('{"key":"val"}');
┌─────────────────────────────┐
│ check_json('{"key":"val"}') │
├─────────────────────────────┤
│ NULL                        │
└─────────────────────────────┘

SELECT check_json('{"key":');
┌──────────────────────────────────────────────┐
│ check_json('{"key":')                        │
├──────────────────────────────────────────────┤
│ EOF while parsing a value at line 1 column 7 │
└──────────────────────────────────────────────┘
```
