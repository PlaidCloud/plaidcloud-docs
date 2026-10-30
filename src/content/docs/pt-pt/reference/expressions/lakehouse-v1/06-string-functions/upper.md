---
title: UPPER (Lakehouse v1)
description: UPPER — devolve uma cadeia de caracteres com todos os carateres convertidos em maiúsculas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/upper.md
---

Devolve uma cadeia de caracteres com todos os carateres convertidos em maiúsculas.

## Sintaxe do Analyze

```python
func.unhex(<expr>)
```

## Exemplos do Analyze

```python
func.upper('hello, plaidcloud lakehouse!')
┌────────────────────────────────────────────┐
│ func.upper('hello, plaidcloud lakehouse!') │
├────────────────────────────────────────────┤
│ 'HELLO, PLAIDCLOUD LAKEHOUSE!'             │
└────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
UPPER(<str>)
```

## Aliases

- [UCASE](../ucase)

## Tipo de retorno

VARCHAR

## Exemplos de SQL

```sql
SELECT UPPER('hello, databend!'), UCASE('hello, databend!');

┌───────────────────────────────────────────────────────┐
│ upper('hello, databend!') │ ucase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ HELLO, DATABEND!          │ HELLO, DATABEND!          │
└───────────────────────────────────────────────────────┘
```
