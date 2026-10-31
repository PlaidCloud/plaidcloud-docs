---
title: TRIM_LEADING (Lakehouse v1)
description: TRIM_LEADING – entfernt alle Vorkommen der angegebenen Trim-Zeichenfolge am Anfang der Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-leading.md
---

Entfernt alle Vorkommen der angegebenen Trim-Zeichenfolge am Anfang der Zeichenfolge.

Siehe auch: 

- [LTRIM](../ltrim)
- [TRIM_TRAILING](../trim-trailing)

## Analyze-Syntax

```python
func.trim_leading(<string>, <trim_string>)
```

## Analyze-Beispiele

```python
func.trim_leading('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_leading('xxdatabendxx', 'x')   │
├──────────────────────────────────────────┤
│ databendxx                               │
└──────────────────────────────────────────┘
```

## SQL-Syntax

```sql
TRIM_LEADING(<string>, <trim_string>)
```

## SQL-Beispiele

```sql
SELECT TRIM_LEADING('xxdatabend', 'xxx'), TRIM_LEADING('xxdatabend', 'xx'), TRIM_LEADING('xxdatabend', 'x');

┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_leading('xxdatabend', 'xxx') │ trim_leading('xxdatabend', 'xx') │ trim_leading('xxdatabend', 'x') │
├───────────────────────────────────┼──────────────────────────────────┼─────────────────────────────────┤
│ xxdatabend                        │ databend                         │ databend                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
