---
title: LPAD (Lakehouse v1)
description: LPAD — zwraca ciąg znaków str dopełniony z lewej strony ciągiem padstr do długości len znaków.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/lpad.md
---

Zwraca ciąg znaków str dopełniony z lewej strony ciągiem padstr do długości len znaków.
Jeśli str jest dłuższy niż len, zwracana wartość jest skracana do len znaków.

## Składnia Analyze

```python
func.lpad(<str>, <len>, <padstr>)
```

## Przykłady Analyze

```python
func.lpad('hi',4,'??')
┌────────────────────────┐
│ func.lpad('hi',4,'??') │
├────────────────────────┤
│ ??hi                   │
└────────────────────────┘
```

```python
func.lpad('hi',1,'??')
┌────────────────────────┐
│ func.lpad('hi',1,'??') │
├────────────────────────┤
│ h                      │
└────────────────────────┘
```

## Składnia SQL

```sql
LPAD(<str>, <len>, <padstr>)
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
SELECT LPAD('hi',4,'??');
┌─────────────────────┐
│ LPAD('hi', 4, '??') │
├─────────────────────┤
│ ??hi                │
└─────────────────────┘

SELECT LPAD('hi',1,'??');
┌─────────────────────┐
│ LPAD('hi', 1, '??') │
├─────────────────────┤
│ h                   │
└─────────────────────┘
```
