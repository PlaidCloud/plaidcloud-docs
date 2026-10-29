---
title: TRIM_TRAILING (Lakehouse v1)
description: TRIM_TRAILING – entfernt alle Vorkommen der angegebenen Trim-Zeichenfolge am Ende der Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-trailing.md
---

Entfernt alle Vorkommen der angegebenen Trim-Zeichenfolge am Ende der Zeichenfolge.

Siehe auch: 

- [RTRIM](../rtrim)
- [TRIM_LEADING](../trim-leading)

## Analyze-Syntax

```python
func.trim_trailing(<string>, <trim_string>)
```

## Analyze-Beispiele

```python
func.trim_trailing('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_trailing('xxdatabendxx', 'x')  │
├──────────────────────────────────────────┤
│ xxdatabend                               │
└──────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TRIM_TRAILING(<string>, <trim_string>)
```

## SQL-Beispiele

```sql
SELECT TRIM_TRAILING('databendxx', 'xxx'), TRIM_TRAILING('databendxx', 'xx'), TRIM_TRAILING('databendxx', 'x');

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_trailing('databendxx', 'xxx') │ trim_trailing('databendxx', 'xx') │ trim_trailing('databendxx', 'x') │
├────────────────────────────────────┼───────────────────────────────────┼──────────────────────────────────┤
│ databendxx                         │ databend                          │ databend                         │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
