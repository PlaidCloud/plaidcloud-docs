---
title: CONCAT (Lakehouse v1)
description: CONCAT — devuelve la cadena que resulta de concatenar los argumentos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/concat.md
---

Devuelve la cadena que resulta de concatenar los argumentos. Puede tener uno o más argumentos. Si todos los argumentos son cadenas no binarias, el resultado es una cadena no binaria. Si los argumentos incluyen alguna cadena binaria, el resultado es una cadena binaria. Un argumento numérico se convierte a su forma equivalente de cadena no binaria.

## Sintaxis de Analyze

```python
func.concat(<expr1>, ...)
```

## Ejemplos de Analyze

```python
func.concat('data', 'bend')
┌─────────────────────────────┐
│ func.concat('data', 'bend') │
├─────────────────────────────┤
│ databend                    │
└─────────────────────────────┘
```

## Sintaxis SQL

```sql
CONCAT(<expr1>, ...)
```

## Argumentos

| Argumentos | Descripción |
|-----------|-------------|
| `<expr1>` | cadena      |

## Tipo de retorno

Un valor de tipo de datos `VARCHAR` o de tipo de datos `NULL`.

## Ejemplos de SQL

```sql
SELECT CONCAT('data', 'bend');
┌────────────────────────┐
│ concat('data', 'bend') │
├────────────────────────┤
│ databend               │
└────────────────────────┘

SELECT CONCAT('data', NULL, 'bend');
┌──────────────────────────────┐
│ CONCAT('data', NULL, 'bend') │
├──────────────────────────────┤
│                         NULL │
└──────────────────────────────┘

SELECT CONCAT('14.3');
┌────────────────┐
│ concat('14.3') │
├────────────────┤
│ 14.3           │
└────────────────┘
```
