---
title: LENGTH (Lakehouse v1)
description: LENGTH — zwraca długość podanego ciągu znaków lub wartości binarnej.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/length.md
---

Zwraca długość podanego ciągu znaków lub wartości binarnej. W przypadku ciągów znaków długość oznacza liczbę znaków, przy czym każdy znak UTF-8 jest liczony jako jeden znak. W przypadku danych binarnych długość odpowiada liczbie bajtów.

## Składnia Analyze

```python
func.length(<expr>)
```

## Przykłady Analyze

```python
func.length('Hello')
┌──────────────────────┐
│ func.length('Hello') │
├──────────────────────┤
│                    5 │
└──────────────────────┘
```

## Składnia SQL

```sql
LENGTH(<expr>)
```

## Aliasy

- [CHAR_LENGTH](../char-length)
- [CHARACTER_LENGTH](../character-length)
- [LENGTH_UTF8](../length-utf8)

## Typ zwracany

BIGINT

## Przykłady SQL

```sql
SELECT LENGTH('Hello'), LENGTH_UTF8('Hello'), CHAR_LENGTH('Hello'), CHARACTER_LENGTH('Hello');

┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ length('hello') │ length_utf8('hello') │ char_length('hello') │ character_length('hello') │
├─────────────────┼──────────────────────┼──────────────────────┼───────────────────────────┤
│               5 │                    5 │                    5 │                         5 │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```
