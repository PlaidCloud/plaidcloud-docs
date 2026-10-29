---
title: RTRIM (Lakehouse v1)
description: RTRIM — usuwa z prawej strony ciągu znaków wszystkie wystąpienia dowolnego znaku zawartego w podanym ciągu przycinającym.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/rtrim.md
---

Usuwa z prawej strony ciągu znaków wszystkie wystąpienia dowolnego znaku zawartego w podanym ciągu przycinającym.

Zobacz także: 

- [TRIM_TRAILING](../trim-trailing)
- [LTRIM](../ltrim)

## Składnia Analyze

```python
func.rtrim(<string>, <trim_string>)
```

## Przykłady Analyze

```python
func.rtrim('databend'xx, 'x')
┌────────────────────────────────┐
│ func.rtrim('databendxx', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## Składnia SQL

```sql
RTRIM(<string>, <trim_string>)
```

## Przykłady SQL

```sql
SELECT RTRIM('databendxx', 'x'), RTRIM('databendxx', 'xy');

┌──────────────────────────────────────────────────────┐
│ rtrim('databendxx', 'x') │ rtrim('databendxx', 'xy') │
├──────────────────────────┼───────────────────────────┤
│ databend                 │ databend                  │
└──────────────────────────────────────────────────────┘
```
