---
title: UNHEX (Lakehouse v1)
description: "UNHEX: para un argumento de cadena str, UNHEX(str) interpreta cada par de caracteres del argumento."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/unhex.md
---

Para un argumento de cadena str, UNHEX(str) interpreta cada par de caracteres del argumento como un número hexadecimal y lo convierte en el byte que representa ese número. El valor devuelto es una cadena binaria.

## Sintaxis de Analyze

```python
func.unhex(<expr>)
```

## Ejemplos de Analyze

```python
func.unhex('6461746162656e64')
┌────────────────────────────────┐
│ func.unhex('6461746162656e64') │
├────────────────────────────────┤
│ 6461746162656E64               │
└────────────────────────────────┘
```

## Sintaxis de SQL

```sql
UNHEX(<expr>)
```

## Alias

- [FROM_HEX](../from-hex)

## Ejemplos de SQL

```sql
SELECT UNHEX('6461746162656e64') as c1, typeof(c1),UNHEX('6461746162656e64')::varchar as c2, typeof(c2), FROM_HEX('6461746162656e64');

┌─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│           c1              │     typeof(c1)         │       c2         |    typeof(c2)     |   from_hex('6461746162656e64')  |
├───────────────────────────┼────────────────────────|──────────────────┤───────────────────|─────────────────────────────────┤
│ 6461746162656E64          │      binary            │      databend    |    varchar        |   6461746162656E64              |
└─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT UNHEX(HEX('string')), unhex(HEX('string'))::varchar;

┌──────────────────────────────────────────────────────┐
│ unhex(hex('string')) │ unhex(hex('string'))::varchar │
├──────────────────────┼───────────────────────────────┤
│ 737472696E67         │ string                        │
└──────────────────────────────────────────────────────┘
```
