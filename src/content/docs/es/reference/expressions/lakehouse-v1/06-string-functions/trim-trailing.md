---
title: TRIM_TRAILING (Lakehouse v1)
description: "TRIM_TRAILING: elimina todas las apariciones de la cadena de recorte especificada al final de la cadena."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-trailing.md
---

Elimina todas las apariciones de la cadena de recorte especificada al final de la cadena.

Consulte también: 

- [RTRIM](../rtrim)
- [TRIM_LEADING](../trim-leading)

## Sintaxis de Analyze

```python
func.trim_trailing(<string>, <trim_string>)
```

## Ejemplos de Analyze

```python
func.trim_trailing('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_trailing('xxdatabendxx', 'x')  │
├──────────────────────────────────────────┤
│ xxdatabend                               │
└──────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TRIM_TRAILING(<string>, <trim_string>)
```

## Ejemplos de SQL

```sql
SELECT TRIM_TRAILING('databendxx', 'xxx'), TRIM_TRAILING('databendxx', 'xx'), TRIM_TRAILING('databendxx', 'x');

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_trailing('databendxx', 'xxx') │ trim_trailing('databendxx', 'xx') │ trim_trailing('databendxx', 'x') │
├────────────────────────────────────┼───────────────────────────────────┼──────────────────────────────────┤
│ databendxx                         │ databend                          │ databend                         │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
