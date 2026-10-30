---
title: TRIM_TRAILING (Lakehouse v1)
description: TRIM_TRAILING — remove todas as ocorrências da string de corte especificada do final da string.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-trailing.md
---

Remove todas as ocorrências da string de corte especificada do final da string.

Veja também: 

- [RTRIM](../rtrim)
- [TRIM_LEADING](../trim-leading)

## Sintaxe do Analyze

```python
func.trim_trailing(<string>, <trim_string>)
```

## Exemplos do Analyze

```python
func.trim_trailing('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_trailing('xxdatabendxx', 'x')  │
├──────────────────────────────────────────┤
│ xxdatabend                               │
└──────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
TRIM_TRAILING(<string>, <trim_string>)
```

## Exemplos de SQL

```sql
SELECT TRIM_TRAILING('databendxx', 'xxx'), TRIM_TRAILING('databendxx', 'xx'), TRIM_TRAILING('databendxx', 'x');

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_trailing('databendxx', 'xxx') │ trim_trailing('databendxx', 'xx') │ trim_trailing('databendxx', 'x') │
├────────────────────────────────────┼───────────────────────────────────┼──────────────────────────────────┤
│ databendxx                         │ databend                          │ databend                         │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
