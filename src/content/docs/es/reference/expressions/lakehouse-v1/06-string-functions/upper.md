---
title: UPPER (Lakehouse v1)
description: "UPPER: devuelve una cadena con todos los caracteres convertidos a mayúsculas."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/upper.md
---

Devuelve una cadena con todos los caracteres convertidos a mayúsculas.

## Sintaxis de Analyze

```python
func.unhex(<expr>)
```

## Ejemplos de Analyze

```python
func.upper('hello, plaidcloud lakehouse!')
┌────────────────────────────────────────────┐
│ func.upper('hello, plaidcloud lakehouse!') │
├────────────────────────────────────────────┤
│ 'HELLO, PLAIDCLOUD LAKEHOUSE!'             │
└────────────────────────────────────────────┘
```

## Sintaxis de SQL

```sql
UPPER(<str>)
```

## Alias

- [UCASE](../ucase)

## Tipo de valor devuelto

VARCHAR

## Ejemplos de SQL

```sql
SELECT UPPER('hello, databend!'), UCASE('hello, databend!');

┌───────────────────────────────────────────────────────┐
│ upper('hello, databend!') │ ucase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ HELLO, DATABEND!          │ HELLO, DATABEND!          │
└───────────────────────────────────────────────────────┘
```
