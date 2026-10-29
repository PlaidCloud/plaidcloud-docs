---
title: LOWER (Lakehouse v1)
description: LOWER — devolve uma cadeia de caracteres com todos os caracteres convertidos em minúsculas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/lower.md
---

Devolve uma cadeia de caracteres com todos os caracteres convertidos em minúsculas.

## Sintaxe do Analyze

```python
func.lower(<str>)
```

## Exemplos do Analyze

```python
func.lower('Hello, PlaidCloud!')
┌──────────────────────────────────┐
│ func.lower('Hello, PlaidCloud!') │
├──────────────────────────────────┤
│ hello, plaidcloud!               │
└──────────────────────────────────┘
```

## Sintaxe SQL

```sql
LOWER(<str>)
```

## Aliases

- [LCASE](../lcase)

## Tipo de Retorno

VARCHAR

## Exemplos SQL

```sql
SELECT LOWER('Hello, Databend!'), LCASE('Hello, Databend!');

┌───────────────────────────────────────────────────────┐
│ lower('hello, databend!') │ lcase('hello, databend!') │
├───────────────────────────┼───────────────────────────┤
│ hello, databend!          │ hello, databend!          │
└───────────────────────────────────────────────────────┘
```
