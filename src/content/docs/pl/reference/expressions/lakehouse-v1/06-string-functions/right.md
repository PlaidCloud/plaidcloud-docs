---
title: RIGHT (Lakehouse v1)
description: RIGHT — zwraca len znaków z prawej strony ciągu str lub NULL, jeśli którykolwiek argument ma wartość NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/right.md
---

Zwraca len znaków z prawej strony ciągu str lub NULL, jeśli którykolwiek argument ma wartość NULL.

## Składnia Analyze

```python
func.right(<str>, <len>)
```

## Przykłady Analyze

```python
func.right('foobarbar', 4)
┌────────────────────────────┐
│ func.right('foobarbar', 4) │
├────────────────────────────┤
│ rbar                       │
└────────────────────────────┘
```

## Składnia SQL

```sql
RIGHT(<str>, <len>);
```

## Argumenty

| Argumenty | Opis                                                   |
|-----------|--------------------------------------------------------|
| `<str>`   | Główny ciąg znaków, z którego są wyodrębniane znaki    |
| `<len>`   | Liczba znaków                                          |

## Typ zwracany

`VARCHAR`

## Przykłady SQL

```sql
SELECT RIGHT('foobarbar', 4);
┌───────────────────────┐
│ RIGHT('foobarbar', 4) │
├───────────────────────┤
│ rbar                  │
└───────────────────────┘
```
