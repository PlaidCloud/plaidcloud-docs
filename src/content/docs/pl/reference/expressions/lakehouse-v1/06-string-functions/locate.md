---
title: LOCATE (Lakehouse v1)
description: LOCATE — pierwsza składnia zwraca pozycję pierwszego wystąpienia podciągu substr w ciągu znaków str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/locate.md
---

Pierwsza składnia zwraca pozycję pierwszego wystąpienia podciągu substr w ciągu znaków str.
Druga składnia zwraca pozycję pierwszego wystąpienia podciągu substr w ciągu znaków str, zaczynając od pozycji pos.
Zwraca 0, jeśli substr nie występuje w str. Zwraca NULL, jeśli którykolwiek argument ma wartość NULL.

## Składnia Analyze

```python
func.locate(<substr>, <str>, <pos>)
```

## Przykłady Analyze

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

## Składnia SQL

```sql
LOCATE(<substr>, <str>)
LOCATE(<substr>, <str>, <pos>)
```

## Argumenty

| Argumenty  | Opis         |
|------------|--------------|
| `<substr>` | Podciąg.     |
| `<str>`    | Ciąg znaków. |
| `<pos>`    | Pozycja.     |

## Typ zwracany

`BIGINT`

## Przykłady SQL

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
