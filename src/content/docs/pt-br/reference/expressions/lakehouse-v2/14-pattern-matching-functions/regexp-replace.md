---
title: REGEXP_REPLACE (Lakehouse v2)
description: "Use a função de correspondência de padrões REGEXP_REPLACE no PlaidCloud Lakehouse. Substitui as substrings que correspondem a um padrão de expressão regular por uma string de substituição."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-replace.md
---

Substitui as substrings que correspondem a um padrão de expressão regular por uma string de substituição.

## Sintaxe do Analyze

```python
func.regexp_replace(<str>, <pattern>, <replacement>)
```

## Exemplos do Analyze

```python
func.regexp_replace('hello   world', '\\s+', ' ')

┌───────────────┐
│ 'hello world'  │
└───────────────┘
```

## Sintaxe SQL

```sql
REGEXP_REPLACE(<str>, <pattern>, <replacement>)
```

## Exemplos de SQL

```sql
SELECT REGEXP_REPLACE('hello   world', '\\s+', ' ');

┌─────────────┐
│ hello world  │
└─────────────┘
```
