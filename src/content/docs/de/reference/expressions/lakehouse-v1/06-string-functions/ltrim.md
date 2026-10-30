---
title: LTRIM (Lakehouse v1)
description: LTRIM – entfernt alle Vorkommen der Zeichen aus der angegebenen Trim-Zeichenfolge auf der linken Seite der Zeichenfolge.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ltrim.md
---

Entfernt alle Vorkommen der Zeichen aus der angegebenen Trim-Zeichenfolge auf der linken Seite der Zeichenfolge.

Siehe auch: 

- [TRIM_LEADING](../trim-leading)
- [RTRIM](../rtrim)

## Analyze-Syntax

```python
func.ltrim(<string>, <trim_string>)
```

## Analyze-Beispiele

```python
func.ltrim('xxdatabend', 'x')
┌────────────────────────────────┐
│ func.ltrim('xxdatabend', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## SQL-Syntax

```sql
LTRIM(<string>, <trim_string>)
```

## SQL-Beispiele

```sql
SELECT LTRIM('xxdatabend', 'xx'), LTRIM('xxdatabend', 'xy');

┌───────────────────────────────────────────────────────┐
│ ltrim('xxdatabend', 'xx') │ ltrim('xxdatabend', 'xy') │
├───────────────────────────┼───────────────────────────┤
│ databend                  │ databend                  │
└───────────────────────────────────────────────────────┘
```
