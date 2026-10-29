---
title: ASCII (Lakehouse v1)
description: ASCII — devuelve el valor numérico del carácter situado más a la izquierda de la cadena str.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/ascii.md
---

Devuelve el valor numérico del carácter situado más a la izquierda de la cadena str.

## Sintaxis de Analyze

```python
func.ascii(<expr>)
```

## Ejemplos de Analyze

```python
func.ascii('2')
┌─────────────────┐
│ func.ascii('2') │
├─────────────────┤
│              50 │
└─────────────────┘
```

## Sintaxis SQL

```sql
ASCII(<expr>)
```

## Argumentos

| Argumentos | Descripción |
|-----------|-------------|
| `<expr>`  | La cadena. |

## Tipo de retorno

`TINYINT`

## Ejemplos de SQL

```sql
SELECT ASCII('2');
┌────────────┐
│ ASCII('2') │
├────────────┤
│         50 │
└────────────┘
```
