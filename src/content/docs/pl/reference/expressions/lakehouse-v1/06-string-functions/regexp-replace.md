---
title: REGEXP_REPLACE (Lakehouse v1)
description: REGEXP_REPLACE — zastępuje wystąpienia w ciągu znaków expr, które pasują do wyrażenia regularnego.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-replace.md
---

Zastępuje wystąpienia w ciągu znaków `expr`, które pasują do wyrażenia regularnego określonego wzorcem `pat`, ciągiem zastępującym `repl` i zwraca otrzymany ciąg. Jeśli `expr`, `pat` lub `repl` ma wartość NULL, zwracana jest wartość NULL.

## Składnia Analyze

```python
func.regexp_replace(<expr>, <pat>, <repl[, pos[, occurrence[, match_type]]]>)
```

## Przykłady Analyze

```python
func.regexp_replace('a b c', 'b', 'X')
┌────────────────────────────────────────┐
│ func.regexp_replace('a b c', 'b', 'X') │
├────────────────────────────────────────┤
│ a X c                                  │
└────────────────────────────────────────┘
```

## Składnia SQL

```sql
REGEXP_REPLACE(<expr>, <pat>, <repl[, pos[, occurrence[, match_type]]]>)
```

## Argumenty

| Argumenty  | Opis                                                                                                                                    |
|------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| expr       | Ciąg znaków expr, który ma zostać dopasowany                                                                                            |
| pat        | Wyrażenie regularne                                                                                                                     |
| repl       | Ciąg zastępujący                                                                                                                        |
| pos        | Opcjonalny. Pozycja w expr, od której zaczyna się wyszukiwanie. Jeśli pominięto, wartość domyślna to 1.                                 |
| occurrence | Opcjonalny. Które wystąpienie dopasowania zastąpić. Jeśli pominięto, wartość domyślna to 0 (co oznacza „zastąp wszystkie wystąpienia”). |
| match_type | Opcjonalny. Ciąg znaków określający sposób dopasowywania. Znaczenie jest takie samo jak w funkcji REGEXP_LIKE().                        |

## Typ zwracany

`VARCHAR`

## Przykłady SQL

```sql
SELECT REGEXP_REPLACE('a b c', 'b', 'X');
┌───────────────────────────────────┐
│ REGEXP_REPLACE('a b c', 'b', 'X') │
├───────────────────────────────────┤
│ a X c                             │
└───────────────────────────────────┘

SELECT REGEXP_REPLACE('abc def ghi', '[a-z]+', 'X', 1, 3);
┌────────────────────────────────────────────────────┐
│ REGEXP_REPLACE('abc def ghi', '[a-z]+', 'X', 1, 3) │
├────────────────────────────────────────────────────┤
│ abc def X                                          │
└────────────────────────────────────────────────────┘

SELECT REGEXP_REPLACE('周 周周 周周周', '周+', 'X', 3, 2);
┌───────────────────────────────────────────────────────────┐
│ REGEXP_REPLACE('周 周周 周周周', '周+', 'X', 3, 2)        │
├───────────────────────────────────────────────────────────┤
│ 周 周周 X                                                 │
└───────────────────────────────────────────────────────────┘
```
