---
title: TRIM_BOTH (Lakehouse v1)
description: TRIM_BOTH – entfernt alle Vorkommen der angegebenen Trim-Zeichenfolge am Anfang, am Ende oder auf beiden Seiten der Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-both.md
---

Entfernt alle Vorkommen der angegebenen Trim-Zeichenfolge am Anfang, am Ende oder auf beiden Seiten der Zeichenfolge.

Siehe auch: [TRIM](../trim)

## Analyze-Syntax

```python
func.trim_both(<string>, <trim_string>)
```

## Analyze-Beispiele

```python
func.trim_both('xxdatabendxx', 'x')
┌──────────────────────────────────────┐
│ func.trim_both('xxdatabendxx', 'x')  │
├──────────────────────────────────────┤
│ databend                             │
└──────────────────────────────────────┘
```

## SQL-Syntax

```sql
TRIM_BOTH(<string>, <trim_string>)
```

## SQL-Beispiele

```sql
SELECT TRIM_BOTH('xxdatabendxx', 'xxx'), TRIM_BOTH('xxdatabendxx', 'xx'), TRIM_BOTH('xxdatabendxx', 'x');

┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_both('xxdatabendxx', 'xxx') │ trim_both('xxdatabendxx', 'xx') │ trim_both('xxdatabendxx', 'x') │
├──────────────────────────────────┼─────────────────────────────────┼────────────────────────────────┤
│ xxdatabendxx                     │ databend                        │ databend                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
