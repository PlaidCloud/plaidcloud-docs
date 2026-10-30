---
title: REGEXP_SPLIT (Lakehouse v2)
description: REGEXP_SPLIT — divide uma string por um padrão de expressão regular e retorna um array de substrings.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/regexp-split.md
---

Divide uma string por um padrão de expressão regular e retorna um array de substrings.

## Sintaxe do Analyze

```python
func.regexp_split('one1two2three', '[0-9]')
```

## Exemplos do Analyze

```python
func.regexp_split('one1two2three', '[0-9]')

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```

## Sintaxe SQL

```sql
REGEXP_SPLIT(<str>, <pattern>)
```

## Exemplos de SQL

```sql
SELECT REGEXP_SPLIT('one1two2three', '[0-9]');

┌───────────────────────┐
│ ["one","two","three"] │
└───────────────────────┘
```
