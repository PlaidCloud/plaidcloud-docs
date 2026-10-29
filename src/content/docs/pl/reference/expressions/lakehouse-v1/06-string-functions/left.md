---
title: LEFT (Lakehouse v1)
description: LEFT — zwraca len znaków z lewej strony ciągu str lub NULL, jeśli którykolwiek argument ma wartość NULL.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/left.md
---

Zwraca len znaków z lewej strony ciągu str lub NULL, jeśli którykolwiek argument ma wartość NULL.

## Składnia Analyze

```python
func.left(<str>, <len>)
```

## Przykłady Analyze

```python
func.left('foobarbar', 5)
┌───────────────────────────┐
│ func.left('foobarbar', 5) │
├───────────────────────────┤
│ fooba                     │
└───────────────────────────┘
```

## Składnia SQL

```sql
LEFT(<str>, <len>);
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
SELECT LEFT('foobarbar', 5);
┌──────────────────────┐
│ LEFT('foobarbar', 5) │
├──────────────────────┤
│ fooba                │
└──────────────────────┘
```
