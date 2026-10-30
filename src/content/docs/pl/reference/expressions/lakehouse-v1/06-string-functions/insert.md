---
title: INSERT (Lakehouse v1)
description: INSERT — zwraca ciąg znaków str, w którym podciąg zaczynający się na pozycji pos i mający długość len znaków został zastąpiony ciągiem newstr.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/insert.md
---

Zwraca ciąg znaków str, w którym podciąg zaczynający się na pozycji pos i mający długość len znaków został zastąpiony ciągiem newstr. Zwraca oryginalny ciąg, jeśli pos nie mieści się w długości ciągu. Zastępuje resztę ciągu od pozycji pos, jeśli len przekracza długość pozostałej części ciągu. Zwraca NULL, jeśli którykolwiek argument ma wartość NULL.

## Składnia Analyze

```python
func.insert(<str>, <pos>, <len>, <newstr>)
```

## Przykłady Analyze

```python
func.insert('Quadratic', 3, 4, 'What')
┌────────────────────────────────────────┐
│ func.insert('Quadratic', 3, 4, 'What') │
├────────────────────────────────────────┤
│ QuWhattic                              │
└────────────────────────────────────────┘
```

## Składnia SQL

```sql
INSERT(<str>, <pos>, <len>, <newstr>)
```

## Argumenty

| Argumenty  | Opis             |
|------------|------------------|
| `<str>`    | Ciąg znaków.     |
| `<pos>`    | Pozycja.         |
| `<len>`    | Długość.         |
| `<newstr>` | Nowy ciąg znaków.|

## Typ zwracany

`VARCHAR`

## Przykłady SQL

```sql
SELECT INSERT('Quadratic', 3, 4, 'What');
┌───────────────────────────────────┐
│ INSERT('Quadratic', 3, 4, 'What') │
├───────────────────────────────────┤
│ QuWhattic                         │
└───────────────────────────────────┘

SELECT INSERT('Quadratic', -1, 4, 'What');
┌───────────────────────────────────────┐
│ INSERT('Quadratic', (- 1), 4, 'What') │
├───────────────────────────────────────┤
│ Quadratic                             │
└───────────────────────────────────────┘

SELECT INSERT('Quadratic', 3, 100, 'What');
┌─────────────────────────────────────┐
│ INSERT('Quadratic', 3, 100, 'What') │
├─────────────────────────────────────┤
│ QuWhat                              │
└─────────────────────────────────────┘

┌────────────────────────────────────────────┬────────┐
│ INSERT('123456789', number, number, 'aaa') │ number │
├────────────────────────────────────────────┼────────┤
│ 123456789                                  │      0 │
│ aaa23456789                                │      1 │
│ 1aaa456789                                 │      2 │
│ 12aaa6789                                  │      3 │
│ 123aaa89                                   │      4 │
│ 1234aaa                                    │      5 │
│ 12345aaa                                   │      6 │
│ 123456aaa                                  │      7 │
│ 1234567aaa                                 │      8 │
│ 12345678aaa                                │      9 │
│ 123456789                                  │     10 │
│ 123456789                                  │     11 │
│ 123456789                                  │     12 │
└────────────────────────────────────────────┴────────┘
```
