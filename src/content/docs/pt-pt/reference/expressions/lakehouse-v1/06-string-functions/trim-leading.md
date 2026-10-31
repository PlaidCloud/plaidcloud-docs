---
title: TRIM_LEADING (Lakehouse v1)
description: TRIM_LEADING — remove todas as ocorrências da cadeia de corte especificada do início da cadeia de caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-leading.md
---

Remove todas as ocorrências da cadeia de corte especificada do início da cadeia de caracteres.

Consulte também: 

- [LTRIM](../ltrim)
- [TRIM_TRAILING](../trim-trailing)

## Sintaxe do Analyze

```python
func.trim_leading(<string>, <trim_string>)
```

## Exemplos do Analyze

```python
func.trim_leading('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_leading('xxdatabendxx', 'x')   │
├──────────────────────────────────────────┤
│ databendxx                               │
└──────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TRIM_LEADING(<string>, <trim_string>)
```

## Exemplos de SQL

```sql
SELECT TRIM_LEADING('xxdatabend', 'xxx'), TRIM_LEADING('xxdatabend', 'xx'), TRIM_LEADING('xxdatabend', 'x');

┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_leading('xxdatabend', 'xxx') │ trim_leading('xxdatabend', 'xx') │ trim_leading('xxdatabend', 'x') │
├───────────────────────────────────┼──────────────────────────────────┼─────────────────────────────────┤
│ xxdatabend                        │ databend                         │ databend                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
