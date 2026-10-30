---
title: CONCAT (Lakehouse v1)
description: CONCAT — zwraca ciąg znaków powstały z połączenia argumentów.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/concat.md
---

Zwraca ciąg znaków powstały z połączenia argumentów. Może przyjmować jeden lub więcej argumentów. Jeśli wszystkie argumenty są ciągami niebinarnymi, wynikiem jest ciąg niebinarny. Jeśli wśród argumentów jest choć jeden ciąg binarny, wynikiem jest ciąg binarny. Argument liczbowy jest konwertowany na równoważną niebinarną postać tekstową.

## Składnia Analyze

```python
func.concat(<expr1>, ...)
```

## Przykłady Analyze

```python
func.concat('data', 'bend')
┌─────────────────────────────┐
│ func.concat('data', 'bend') │
├─────────────────────────────┤
│ databend                    │
└─────────────────────────────┘
```

## Składnia SQL

```sql
CONCAT(<expr1>, ...)
```

## Argumenty

| Argumenty | Opis         |
|-----------|--------------|
| `<expr1>` | ciąg znaków  |

## Typ zwracany

Wartość typu danych `VARCHAR` lub typ danych `NULL`.

## Przykłady SQL

```sql
SELECT CONCAT('data', 'bend');
┌────────────────────────┐
│ concat('data', 'bend') │
├────────────────────────┤
│ databend               │
└────────────────────────┘

SELECT CONCAT('data', NULL, 'bend');
┌──────────────────────────────┐
│ CONCAT('data', NULL, 'bend') │
├──────────────────────────────┤
│                         NULL │
└──────────────────────────────┘

SELECT CONCAT('14.3');
┌────────────────┐
│ concat('14.3') │
├────────────────┤
│ 14.3           │
└────────────────┘
```
