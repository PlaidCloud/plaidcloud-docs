---
title: REGEXP_INSTR (Lakehouse v1)
description: REGEXP_INSTR — zwraca początkowy indeks podciągu ciągu znaków expr pasującego do wyrażenia regularnego określonego wzorcem pat lub 0, jeśli nie ma dopasowania.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-instr.md
---

Zwraca początkowy indeks podciągu ciągu znaków `expr` pasującego do wyrażenia regularnego określonego wzorcem `pat` lub `0`, jeśli nie ma dopasowania. Jeśli `expr` lub `pat` ma wartość NULL, zwracana jest wartość NULL. Indeksy znaków zaczynają się od `1`.

## Składnia Analyze

```python
func.regexp_instr(<expr>, <pat[, pos[, occurrence[, return_option[, match_type]]]]>)
```

## Przykłady Analyze

```python
func.regexp_instr('dog cat dog', 'dog')
┌─────────────────────────────────────────┐
│ func.regexp_instr('dog cat dog', 'dog') │
├─────────────────────────────────────────┤
│                                       1 │
└─────────────────────────────────────────┘
```

## Składnia SQL

```sql
REGEXP_INSTR(<expr>, <pat[, pos[, occurrence[, return_option[, match_type]]]]>)
```

## Argumenty

| Argumenty     | Opis                                                                                                                                                                                                                                                                                             |
|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| expr          | Ciąg znaków expr, który ma zostać dopasowany                                                                                                                                                                                                                                                     |
| pat           | Wyrażenie regularne                                                                                                                                                                                                                                                                              |
| pos           | Opcjonalny. Pozycja w expr, od której zaczyna się wyszukiwanie. Jeśli pominięto, wartość domyślna to 1.                                                                                                                                                                                          |
| occurrence    | Opcjonalny. Które wystąpienie dopasowania wyszukać. Jeśli pominięto, wartość domyślna to 1.                                                                                                                                                                                                      |
| return_option | Opcjonalny. Jaki rodzaj pozycji zwrócić. Jeśli wartość wynosi 0, REGEXP_INSTR() zwraca pozycję pierwszego znaku dopasowanego podciągu. Jeśli wartość wynosi 1, REGEXP_INSTR() zwraca pozycję następującą po dopasowanym podciągu. Jeśli pominięto, wartość domyślna to 0.                         |
| match_type    | Opcjonalny. Ciąg znaków określający sposób dopasowywania. Znaczenie jest takie samo jak w funkcji REGEXP_LIKE().                                                                                                                                                                                 |

## Typ zwracany

Wartość typu liczbowego.

## Przykłady SQL

```sql
SELECT REGEXP_INSTR('dog cat dog', 'dog');
┌────────────────────────────────────┐
│ REGEXP_INSTR('dog cat dog', 'dog') │
├────────────────────────────────────┤
│                                  1 │
└────────────────────────────────────┘

SELECT REGEXP_INSTR('dog cat dog', 'dog', 2);
┌───────────────────────────────────────┐
│ REGEXP_INSTR('dog cat dog', 'dog', 2) │
├───────────────────────────────────────┤
│                                     9 │
└───────────────────────────────────────┘

SELECT REGEXP_INSTR('aa aaa aaaa', 'a{2}');
┌─────────────────────────────────────┐
│ REGEXP_INSTR('aa aaa aaaa', 'a{2}') │
├─────────────────────────────────────┤
│                                   1 │
└─────────────────────────────────────┘

SELECT REGEXP_INSTR('aa aaa aaaa', 'a{4}');
┌─────────────────────────────────────┐
│ REGEXP_INSTR('aa aaa aaaa', 'a{4}') │
├─────────────────────────────────────┤
│                                   8 │
└─────────────────────────────────────┘
```
