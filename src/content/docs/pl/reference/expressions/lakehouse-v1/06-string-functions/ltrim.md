---
title: LTRIM (Lakehouse v1)
description: LTRIM — usuwa z lewej strony ciągu znaków wszystkie wystąpienia dowolnego znaku zawartego w podanym ciągu przycinającym.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ltrim.md
---

Usuwa z lewej strony ciągu znaków wszystkie wystąpienia dowolnego znaku zawartego w podanym ciągu przycinającym.

Zobacz także: 

- [TRIM_LEADING](../trim-leading)
- [RTRIM](../rtrim)

## Składnia Analyze

```python
func.ltrim(<string>, <trim_string>)
```

## Przykłady Analyze

```python
func.ltrim('xxdatabend', 'x')
┌────────────────────────────────┐
│ func.ltrim('xxdatabend', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## Składnia SQL

```sql
LTRIM(<string>, <trim_string>)
```

## Przykłady SQL

```sql
SELECT LTRIM('xxdatabend', 'xx'), LTRIM('xxdatabend', 'xy');

┌───────────────────────────────────────────────────────┐
│ ltrim('xxdatabend', 'xx') │ ltrim('xxdatabend', 'xy') │
├───────────────────────────┼───────────────────────────┤
│ databend                  │ databend                  │
└───────────────────────────────────────────────────────┘
```
