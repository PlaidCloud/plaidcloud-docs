---
title: SUBSTR (Lakehouse v1)
description: SUBSTR — wyodrębnia ciąg znaków o określonej liczbie znaków, zaczynając od podanej pozycji.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/substr.md
---

Wyodrębnia z podanego ciągu znaków fragment o określonej liczbie znaków, zaczynając od wskazanej pozycji.

- Formy bez argumentu `len` zwracają podciąg ciągu `str` zaczynający się na pozycji `pos`.
- Formy z argumentem `len` zwracają podciąg ciągu `str` o długości `len` znaków, zaczynający się na pozycji `pos`.

Dla `pos` można też użyć wartości ujemnej. W takim przypadku początek podciągu znajduje się pos znaków od końca ciągu, a nie od jego początku. Wartość ujemną można stosować dla `pos` w każdej formie tej funkcji. Wartość 0 dla `pos` zwraca pusty ciąg. Pozycja pierwszego znaku w ciągu, z którego wyodrębniany jest podciąg, jest liczona jako 1.

## Składnia Analyze

```python
func.substr(<str>, <pos>, <len>)
```

## Przykłady Analyze

```python
func.substr('Quadratically', 5, 6)
┌────────────────────────────────────┐
│ func.substr('Quadratically', 5, 6) │
├────────────────────────────────────┤
│ ratica                             │
└────────────────────────────────────┘
```

## Składnia SQL

```sql
SUBSTR(<str>, <pos>)

SUBSTR(<str>, <pos>, <len>)
```

## Argumenty

| Argumenty | Opis                                                                                                       |
|-----------|------------------------------------------------------------------------------------------------------------|
| `<str>`   | Główny ciąg znaków, z którego są wyodrębniane znaki                                                        |
| `<pos>`   | Pozycja (licząc od 1), od której zaczyna się podciąg. Jeśli jest ujemna, liczona jest od końca            |
| `<len>`   | Maksymalna długość wyodrębnianego podciągu                                                                 |

## Aliasy

- [SUBSTRING](../substring)
- [MID](../mid)

## Typ zwracany

VARCHAR

## Przykłady SQL

```sql
SELECT
  SUBSTRING('Quadratically', 5),
  SUBSTR('Quadratically', 5),
  MID('Quadratically', 5);

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ substring('quadratically' from 5) │ substring('quadratically' from 5) │ mid('quadratically', 5) │
├───────────────────────────────────┼───────────────────────────────────┼─────────────────────────┤
│ ratically                         │ ratically                         │ ratically               │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT
  SUBSTRING('Quadratically', 5, 6),
  SUBSTR('Quadratically', 5, 6),
  MID('Quadratically', 5, 6);

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ substring('quadratically' from 5 for 6) │ substring('quadratically' from 5 for 6) │ mid('quadratically', 5, 6) │
├─────────────────────────────────────────┼─────────────────────────────────────────┼────────────────────────────┤
│ ratica                                  │ ratica                                  │ ratica                     │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
