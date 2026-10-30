---
title: REGEXP_LIKE (Lakehouse v1)
description: REGEXP_LIKE — funkcja REGEXP_LIKE sprawdza, czy ciąg znaków pasuje do wyrażenia regularnego.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-like.md
---

Funkcja REGEXP_LIKE sprawdza, czy ciąg znaków pasuje do wyrażenia regularnego.

## Składnia Analyze

```python
func.regexp_like(<expr>, <pat[, match_type]>)
```

## Przykłady Analyze

```python
func.regexp_like('a', '^[a-d]')
┌─────────────────────────────────┐
│ func.regexp_like('a', '^[a-d]') │
├─────────────────────────────────┤
│                               1 │
└─────────────────────────────────┘
```

## Składnia SQL

```sql
REGEXP_LIKE(<expr>, <pat[, match_type]>)
```

## Argumenty

| Argumenty      | Opis                                                                            |
|----------------|---------------------------------------------------------------------------------|
| `<expr>`       | Ciąg znaków expr, który ma zostać dopasowany                                    |
| `<pat>`        | Wyrażenie regularne                                                             |
| `[match_type]` | Opcjonalny. Argument match_type to ciąg znaków określający sposób dopasowywania |

`match_type` może zawierać dowolne z następujących znaków lub wszystkie:

* `c`: dopasowanie z uwzględnieniem wielkości liter.
* `i`: dopasowanie bez uwzględnienia wielkości liter.
* `m`: tryb wielowierszowy. Rozpoznaje znaki końca wiersza wewnątrz ciągu. Domyślnie znaki końca wiersza są dopasowywane tylko na początku i na końcu wyrażenia tekstowego.
* `n`: znak `.` dopasowuje znaki końca wiersza. Domyślnie dopasowanie `.` kończy się na końcu wiersza.
* `u`: końce wierszy w stylu Uniksa. Nieobsługiwane w tej chwili.

## Typ zwracany

`BIGINT`
Zwraca `1`, jeśli ciąg znaków expr pasuje do wyrażenia regularnego określonego wzorcem pat, w przeciwnym razie `0`. Jeśli expr lub pat ma wartość NULL, zwracana jest wartość NULL.

## Przykłady SQL

```sql
SELECT REGEXP_LIKE('a', '^[a-d]');
┌────────────────────────────┐
│ REGEXP_LIKE('a', '^[a-d]') │
├────────────────────────────┤
│                          1 │
└────────────────────────────┘

SELECT REGEXP_LIKE('abc', 'ABC');
┌───────────────────────────┐
│ REGEXP_LIKE('abc', 'ABC') │
├───────────────────────────┤
│                         1 │
└───────────────────────────┘

SELECT REGEXP_LIKE('abc', 'ABC', 'c');
┌────────────────────────────────┐
│ REGEXP_LIKE('abc', 'ABC', 'c') │
├────────────────────────────────┤
│                              0 │
└────────────────────────────────┘

SELECT REGEXP_LIKE('new*\n*line', 'new\\*.\\*line');

┌───────────────────────────────────────────┐
│ REGEXP_LIKE('new*\n*line', 'new\*.\*line')│
├───────────────────────────────────────────┤
│                                         0 │
└───────────────────────────────────────────┘

SELECT REGEXP_LIKE('new*\n*line', 'new\\*.\\*line', 'n');

┌────────────────────────────────────────────────┐
│ REGEXP_LIKE('new*\n*line', 'new\*.\*line', 'n')│
├────────────────────────────────────────────────┤
│                                              1 │
└────────────────────────────────────────────────┘
```
