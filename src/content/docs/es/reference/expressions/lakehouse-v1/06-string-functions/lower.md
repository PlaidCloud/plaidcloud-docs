---
title: LOWER (Lakehouse v1)
description: LOWER — devuelve una cadena con todos los caracteres convertidos a minúsculas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/lower.md
---

Devuelve una cadena con todos los caracteres convertidos a minúsculas.

## Sintaxis de Analyze

```python
func.lower(<str>)
```

## Ejemplos de Analyze

```python
func.lower('Hello, PlaidCloud!')
┌──────────────────────────────────┐
│ func.lower('Hello, PlaidCloud!') │
├──────────────────────────────────┤
│ hello, plaidcloud!               │
└──────────────────────────────────┘
```

## Sintaxis SQL

```sql
LOWER(<str>)
```

## Alias

- [LCASE](../lcase)

## Tipo de retorno

VARCHAR

## Ejemplos de SQL

```sql
SELECT LOWER('Hello, Databend!'), LCASE('Hello, Databend!');

┌───────────────────────────────────────────────────────┐
│ lower('hello, databend!') │ lcase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ hello, databend!          │ hello, databend!          │
└───────────────────────────────────────────────────────┘
```
