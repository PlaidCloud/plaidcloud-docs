---
title: RPAD (Lakehouse v1)
description: RPAD — zwraca ciąg znaków str dopełniony z prawej strony ciągiem padstr do długości len znaków.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/rpad.md
---

Zwraca ciąg znaków str dopełniony z prawej strony ciągiem padstr do długości len znaków.
Jeśli str jest dłuższy niż len, zwracana wartość jest skracana do len znaków.

## Składnia Analyze

```python
func.rpad(<str>, <len>, <padstr>)
```

## Przykłady Analyze

```python
func.rpad('hi',5,'?')
┌───────────────────────┐
│ func.rpad('hi',5,'?') │
├───────────────────────┤
│ hi???                 │
└───────────────────────┘

func.rpad('hi',1,'?')
┌───────────────────────┐
│ func.rpad('hi',1,'?') │
├───────────────────────┤
│ h                     │
└───────────────────────┘
```

## Składnia SQL

```sql
RPAD(<str>, <len>, <padstr>)
```

## Argumenty

| Argumenty  | Opis                    |
|------------|-------------------------|
| `<str>`    | Ciąg znaków.            |
| `<len>`    | Długość.                |
| `<padstr>` | Ciąg dopełniający.      |

## Typ zwracany

`VARCHAR`

## Przykłady SQL

```sql
SELECT RPAD('hi',5,'?');
┌────────────────────┐
│ RPAD('hi', 5, '?') │
├────────────────────┤
│ hi???              │
└────────────────────┘

SELECT RPAD('hi',1,'?');
┌────────────────────┐
│ RPAD('hi', 1, '?') │
├────────────────────┤
│ h                  │
└────────────────────┘
```
