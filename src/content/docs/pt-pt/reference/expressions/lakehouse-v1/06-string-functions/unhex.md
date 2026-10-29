---
title: UNHEX (Lakehouse v1)
description: UNHEX — para um argumento de cadeia de caracteres str, UNHEX(str) interpreta cada par de carateres do argumento.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/unhex.md
---

Para um argumento de cadeia de caracteres str, UNHEX(str) interpreta cada par de carateres do argumento como um número hexadecimal e converte-o no byte representado por esse número. O valor devolvido é uma cadeia binária.

## Sintaxe do Analyze

```python
func.unhex(<expr>)
```

## Exemplos do Analyze

```python
func.unhex('6461746162656e64')
┌────────────────────────────────┐
│ func.unhex('6461746162656e64') │
├────────────────────────────────┤
│ 6461746162656E64               │
└────────────────────────────────┘
```

## Sintaxe SQL

```sql
UNHEX(<expr>)
```

## Aliases

- [FROM_HEX](../from-hex)

## Exemplos de SQL

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
