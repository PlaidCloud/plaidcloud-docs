---
title: STRCMP (Lakehouse v1)
description: STRCMP — devuelve 0 si las cadenas son iguales, -1 si el primer argumento es menor que el segundo y 1 en caso contrario.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/strcmp.md
---

Devuelve 0 si las cadenas son iguales, -1 si el primer argumento es menor que el segundo y 1 en caso contrario.

## Sintaxis de Analyze

```python
func.strcmp(<expr1> ,<expr2>)
```

## Ejemplos de Analyze

```python
func.strcmp('text', 'text2')
┌──────────────────────────────┐
│ func.strcmp('text', 'text2') │
├──────────────────────────────┤
│                           -1 │
└──────────────────────────────┘

func.strcmp('text2', 'text')
┌──────────────────────────────┐
│ func.strcmp('text2', 'text') │
├──────────────────────────────┤
│                            1 │
└──────────────────────────────┘

func.strcmp('text', 'text')
┌──────────────────────────────┐
│ func.strcmp('text', 'text')  │
├──────────────────────────────┤
│                            0 │
└──────────────────────────────┘
```

## Sintaxis SQL

```sql
STRCMP(<expr1> ,<expr2>)
```

## Argumentos

| Argumentos | Descripción |
|-----------|-------------|
| `<expr1>` | La cadena. |
| `<expr2>` | La cadena. |

## Tipo de retorno

`BIGINT`

## Ejemplos de SQL

```sql
SELECT STRCMP('text', 'text2');
┌─────────────────────────┐
│ STRCMP('text', 'text2') │
├─────────────────────────┤
│                      -1 │
└─────────────────────────┘

SELECT STRCMP('text2', 'text');
┌─────────────────────────┐
│ STRCMP('text2', 'text') │
├─────────────────────────┤
│                       1 │
└─────────────────────────┘

SELECT STRCMP('text', 'text');
┌────────────────────────┐
│ STRCMP('text', 'text') │
├────────────────────────┤
│                      0 │
└────────────────────────┘
```
