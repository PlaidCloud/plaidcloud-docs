---
title: POSITION (Lakehouse v1)
description: POSITION — POSITION(substr IN str) jest synonimem funkcji LOCATE(substr,str).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/position.md
---

POSITION(substr IN str) jest synonimem funkcji LOCATE(substr,str).
Zwraca pozycję pierwszego wystąpienia podciągu substr w ciągu znaków str.
Zwraca 0, jeśli substr nie występuje w str. Zwraca NULL, jeśli którykolwiek argument ma wartość NULL.

## Składnia Analyze

```python
func.position(<substr>, <str>)
```

## Przykłady Analyze

```python
func.position('bar', 'foobarbar')
┌───────────────────────────────────┐
│ func.position('bar', 'foobarbar') │
├───────────────────────────────────┤
│                                 4 │
└───────────────────────────────────┘
```

## Składnia SQL

```sql
POSITION(<substr> IN <str>)
```

## Argumenty

| Argumenty  | Opis         |
|------------|--------------|
| `<substr>` | Podciąg.     |
| `<str>`    | Ciąg znaków. |

## Typ zwracany

`BIGINT`

## Przykłady SQL

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
