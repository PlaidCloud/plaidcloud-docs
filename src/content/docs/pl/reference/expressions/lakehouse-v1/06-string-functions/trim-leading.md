---
title: TRIM_LEADING (Lakehouse v1)
description: TRIM_LEADING — usuwa wszystkie wystąpienia podanego ciągu przycinającego z początku ciągu znaków.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-leading.md
---

Usuwa wszystkie wystąpienia podanego ciągu przycinającego z początku ciągu znaków.

Zobacz też: 

- [LTRIM](../ltrim)
- [TRIM_TRAILING](../trim-trailing)

## Składnia Analyze

```python
func.trim_leading(<string>, <trim_string>)
```

## Przykłady Analyze

```python
func.trim_leading('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_leading('xxdatabendxx', 'x')   │
├──────────────────────────────────────────┤
│ databendxx                               │
└──────────────────────────────────────────┘
```

## Składnia SQL

```sql
TRIM_LEADING(<string>, <trim_string>)
```

## Przykłady SQL

```sql
SELECT TRIM_LEADING('xxdatabend', 'xxx'), TRIM_LEADING('xxdatabend', 'xx'), TRIM_LEADING('xxdatabend', 'x');

┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_leading('xxdatabend', 'xxx') │ trim_leading('xxdatabend', 'xx') │ trim_leading('xxdatabend', 'x') │
├───────────────────────────────────┼──────────────────────────────────┼─────────────────────────────────┤
│ xxdatabend                        │ databend                         │ databend                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
