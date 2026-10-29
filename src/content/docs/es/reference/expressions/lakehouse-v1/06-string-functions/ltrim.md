---
title: LTRIM (Lakehouse v1)
description: LTRIM — elimina todas las apariciones de cualquier carácter presente en la cadena de recorte especificada desde el lado izquierdo de la cadena.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ltrim.md
---

Elimina todas las apariciones de cualquier carácter presente en la cadena de recorte especificada desde el lado izquierdo de la cadena.

Consulte también: 

- [TRIM_LEADING](../trim-leading)
- [RTRIM](../rtrim)

## Sintaxis de Analyze

```python
func.ltrim(<string>, <trim_string>)
```

## Ejemplos de Analyze

```python
func.ltrim('xxdatabend', 'x')
┌────────────────────────────────┐
│ func.ltrim('xxdatabend', 'x')  │
├────────────────────────────────┤
│ databend                       │
└────────────────────────────────┘
```

## Sintaxis SQL

```sql
LTRIM(<string>, <trim_string>)
```

## Ejemplos de SQL

```sql
SELECT LTRIM('xxdatabend', 'xx'), LTRIM('xxdatabend', 'xy');

┌───────────────────────────────────────────────────────┐
│ ltrim('xxdatabend', 'xx') │ ltrim('xxdatabend', 'xy') │
├───────────────────────────┼───────────────────────────┤
│ databend                  │ databend                  │
└───────────────────────────────────────────────────────┘
```
