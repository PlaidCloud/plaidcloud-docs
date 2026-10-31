---
title: TRIM_BOTH (Lakehouse v1)
description: TRIM_BOTH — elimina todas las apariciones de la cadena de recorte especificada al inicio, al final o en ambos lados de la cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim-both.md
---

Elimina todas las apariciones de la cadena de recorte especificada al inicio, al final o en ambos lados de la cadena.

Consulte también: [TRIM](../trim)

## Sintaxis de Analyze

```python
func.trim_both(<string>, <trim_string>)
```

## Ejemplos de Analyze

```python
func.trim_both('xxdatabendxx', 'x')
┌──────────────────────────────────────┐
│ func.trim_both('xxdatabendxx', 'x')  │
├──────────────────────────────────────┤
│ databend                             │
└──────────────────────────────────────┘
```

## Sintaxis SQL

```sql
TRIM_BOTH(<string>, <trim_string>)
```

## Ejemplos de SQL

```sql
SELECT TRIM_BOTH('xxdatabendxx', 'xxx'), TRIM_BOTH('xxdatabendxx', 'xx'), TRIM_BOTH('xxdatabendxx', 'x');

┌─────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ trim_both('xxdatabendxx', 'xxx') │ trim_both('xxdatabendxx', 'xx') │ trim_both('xxdatabendxx', 'x') │
├──────────────────────────────────┼─────────────────────────────────┼────────────────────────────────┤
│ xxdatabendxx                     │ databend                        │ databend                       │
└─────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
