---
title: TRIM_BOTH (Lakehouse v1)
description: TRIM_BOTH — usuwa wszystkie wystąpienia podanego ciągu przycinającego z początku, końca lub obu stron ciągu znaków.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-both.md
---

Usuwa wszystkie wystąpienia podanego ciągu przycinającego z początku, końca lub obu stron ciągu znaków.

Zobacz także: [TRIM](../trim)

## Składnia Analyze

```python
func.trim_both(<string>, <trim_string>)
```

## Przykłady Analyze

```python
func.trim_both('xxdatabendxx', 'x')
┌──────────────────────────────────────┐
│ func.trim_both('xxdatabendxx', 'x')  │
├──────────────────────────────────────┤
│ databend                             │
└──────────────────────────────────────┘
```

## Składnia SQL

```sql
TRIM_BOTH(<string>, <trim_string>)
```

## Przykłady SQL

```sql
SELECT TRIM_BOTH('xxdatabendxx', 'xxx'), TRIM_BOTH('xxdatabendxx', 'xx'), TRIM_BOTH('xxdatabendxx', 'x');

┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_both('xxdatabendxx', 'xxx') │ trim_both('xxdatabendxx', 'xx') │ trim_both('xxdatabendxx', 'x') │
├──────────────────────────────────┼─────────────────────────────────┼────────────────────────────────┤
│ xxdatabendxx                     │ databend                        │ databend                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
