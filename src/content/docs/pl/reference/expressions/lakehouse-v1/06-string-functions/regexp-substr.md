---
title: REGEXP_SUBSTR (Lakehouse v1)
description: REGEXP_SUBSTR — zwraca podciąg ciągu znaków expr, który pasuje do wyrażenia regularnego.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/regexp-substr.md
---

Zwraca podciąg ciągu znaków `expr`, który pasuje do wyrażenia regularnego określonego wzorcem `pat`, lub NULL, jeśli nie ma dopasowania. Jeśli expr lub pat ma wartość NULL, zwracana jest wartość NULL.

## Składnia Analyze

```python
func.regexp_substr(<expr>, <pat[, pos[, occurrence[, match_type]]]>)
```

## Przykłady Analyze

```python
func.regexp_substr('abc def ghi', '[a-z]+')
┌─────────────────────────────────────────────┐
│ func.regexp_substr('abc def ghi', '[a-z]+') │
├─────────────────────────────────────────────┤
│ abc                                         │
└─────────────────────────────────────────────┘
```

## Składnia SQL

```sql
REGEXP_SUBSTR(<expr>, <pat[, pos[, occurrence[, match_type]]]>)
```

## Argumenty

| Argumenty  | Opis                                                                                                             |
|------------|------------------------------------------------------------------------------------------------------------------|
| expr       | Ciąg znaków expr, który ma zostać dopasowany                                                                     |
| pat        | Wyrażenie regularne                                                                                              |
| pos        | Opcjonalny. Pozycja w expr, od której zaczyna się wyszukiwanie. Jeśli pominięto, wartość domyślna to 1.          |
| occurrence | Opcjonalny. Które wystąpienie dopasowania wyszukać. Jeśli pominięto, wartość domyślna to 1.                      |
| match_type | Opcjonalny. Ciąg znaków określający sposób dopasowywania. Znaczenie jest takie samo jak w funkcji REGEXP_LIKE(). |

## Typ zwracany

`VARCHAR`

## Przykłady SQL

```sql
SELECT REGEXP_SUBSTR('abc def ghi', '[a-z]+');
┌────────────────────────────────────────┐
│ REGEXP_SUBSTR('abc def ghi', '[a-z]+') │
├────────────────────────────────────────┤
│ abc                                    │
└────────────────────────────────────────┘

SELECT REGEXP_SUBSTR('abc def ghi', '[a-z]+', 1, 3);
┌──────────────────────────────────────────────┐
│ REGEXP_SUBSTR('abc def ghi', '[a-z]+', 1, 3) │
├──────────────────────────────────────────────┤
│ ghi                                          │
└──────────────────────────────────────────────┘

SELECT REGEXP_SUBSTR('周 周周 周周周 周周周周', '周+', 2, 3);
┌──────────────────────────────────────────────────────────────────┐
│ REGEXP_SUBSTR('周 周周 周周周 周周周周', '周+', 2, 3)            │
├──────────────────────────────────────────────────────────────────┤
│ 周周周周                                                         │
└──────────────────────────────────────────────────────────────────┘

```
