---
title: TRIM_LEADING (Lakehouse v1)
description: "TRIM_LEADING: elimina todas las apariciones de la cadena de recorte especificada al principio de la cadena."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-leading.md
---

Elimina todas las apariciones de la cadena de recorte especificada al principio de la cadena.

Consulte también: 

- [LTRIM](../ltrim)
- [TRIM_TRAILING](../trim-trailing)

## Sintaxis de Analyze

```python
func.trim_leading(<string>, <trim_string>)
```

## Ejemplos de Analyze

```python
func.trim_leading('xxdatabendxx', 'x')
┌──────────────────────────────────────────┐
│ func.trim_leading('xxdatabendxx', 'x')   │
├──────────────────────────────────────────┤
│ databendxx                               │
└──────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
TRIM_LEADING(<string>, <trim_string>)
```

## Ejemplos de SQL

```sql
SELECT TRIM_LEADING('xxdatabend', 'xxx'), TRIM_LEADING('xxdatabend', 'xx'), TRIM_LEADING('xxdatabend', 'x');

┌────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_leading('xxdatabend', 'xxx') │ trim_leading('xxdatabend', 'xx') │ trim_leading('xxdatabend', 'x') │
├───────────────────────────────────┼──────────────────────────────────┼─────────────────────────────────┤
│ xxdatabend                        │ databend                         │ databend                        │
└────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
