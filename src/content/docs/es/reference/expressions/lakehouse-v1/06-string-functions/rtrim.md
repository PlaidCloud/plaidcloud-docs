---
title: RTRIM (Lakehouse v1)
description: RTRIM — elimina todas las apariciones de cualquier carácter presente en la cadena de recorte especificada desde el lado derecho de la cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/rtrim.md
---

Elimina todas las apariciones de cualquier carácter presente en la cadena de recorte especificada desde el lado derecho de la cadena.

Consulte también: 

- [TRIM_TRAILING](../trim-trailing)
- [LTRIM](../ltrim)

## Sintaxis de Analyze

```python
func.rtrim(<string>, <trim_string>)
```

## Ejemplos de Analyze

```python
func.rtrim('databend'xx, 'x')
┌────────────────────────────────┐
│ func.rtrim('databendxx', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## Sintaxis SQL

```sql
RTRIM(<string>, <trim_string>)
```

## Ejemplos de SQL

```sql
SELECT RTRIM('databendxx', 'x'), RTRIM('databendxx', 'xy');

┌──────────────────────────────────────────────────────┐
│ rtrim('databendxx', 'x') │ rtrim('databendxx', 'xy') │
├──────────────────────────┼───────────────────────────┤
│ databend                 │ databend                  │
└──────────────────────────────────────────────────────┘
```
