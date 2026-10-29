---
title: REGEXP_REPLACE (Lakehouse v2)
description: "Utilize a função de correspondência de padrões REGEXP_REPLACE no PlaidCloud Lakehouse. Substitui as subcadeias de caracteres que correspondem a um padrão de expressão regular por uma cadeia de caracteres de substituição."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-replace.md
---

Substitui as subcadeias de caracteres que correspondem a um padrão de expressão regular por uma cadeia de caracteres de substituição.

## Sintaxe de Analyze

```python
func.regexp_replace(<str>, <pattern>, <replacement>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT REGEXP_REPLACE('hello   world', '\\s+', ' ');

┌─────────────┐
│ hello world  │
└─────────────┘
```
