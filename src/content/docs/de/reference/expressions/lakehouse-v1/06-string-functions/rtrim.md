---
title: RTRIM (Lakehouse v1)
description: RTRIM – entfernt alle Vorkommen der Zeichen aus der angegebenen Trim-Zeichenfolge auf der rechten Seite der Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/rtrim.md
---

Entfernt alle Vorkommen der Zeichen aus der angegebenen Trim-Zeichenfolge auf der rechten Seite der Zeichenfolge.

Siehe auch: 

- [TRIM_TRAILING](../trim-trailing)
- [LTRIM](../ltrim)

## Analyze-Syntax

```python
func.rtrim(<string>, <trim_string>)
```

## Analyze-Beispiele

```python
func.rtrim('databend'xx, 'x')
┌────────────────────────────────┐
│ func.rtrim('databendxx', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## SQL-Syntax

```sql
RTRIM(<string>, <trim_string>)
```

## SQL-Beispiele

```sql
SELECT RTRIM('databendxx', 'x'), RTRIM('databendxx', 'xy');

┌──────────────────────────────────────────────────────┐
│ rtrim('databendxx', 'x') │ rtrim('databendxx', 'xy') │
├──────────────────────────┼───────────────────────────┤
│ databend                 │ databend                  │
└──────────────────────────────────────────────────────┘
```
