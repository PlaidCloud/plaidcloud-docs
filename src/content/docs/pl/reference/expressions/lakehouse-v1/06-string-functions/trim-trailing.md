---
title: TRIM_TRAILING (Lakehouse v1)
description: TRIM_TRAILING — usuwa wszystkie wystąpienia podanego ciągu przycinającego z końca ciągu znaków.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-trailing.md
---

Usuwa wszystkie wystąpienia podanego ciągu przycinającego z końca ciągu znaków.

Zobacz też: 

- [RTRIM](../rtrim)
- [TRIM_LEADING](../trim-leading)

## Składnia Analyze

```python
func.trim_trailing(<string>, <trim_string>)
```

## Przykłady Analyze

```python
func.trim_trailing('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_trailing('xxdatabendxx', 'x')  │
├──────────────────────────────────────────┤
│ xxdatabend                               │
└──────────────────────────────────────────┘
```

## Składnia SQL

```sql
TRIM_TRAILING(<string>, <trim_string>)
```

## Przykłady SQL

```sql
SELECT TRIM_TRAILING('databendxx', 'xxx'), TRIM_TRAILING('databendxx', 'xx'), TRIM_TRAILING('databendxx', 'x');

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_trailing('databendxx', 'xxx') │ trim_trailing('databendxx', 'xx') │ trim_trailing('databendxx', 'x') │
├────────────────────────────────────┼───────────────────────────────────┼──────────────────────────────────┤
│ databendxx                         │ databend                          │ databend                         │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
