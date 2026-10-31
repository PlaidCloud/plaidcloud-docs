---
title: REGEXP_COUNT (Lakehouse v2)
description: "Utilize a função de correspondência de padrões REGEXP_COUNT no PlaidCloud Lakehouse. Devolve o número de vezes que um padrão de expressão regular ocorre numa cadeia de caracteres."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-count.md
---

Devolve o número de vezes que um padrão de expressão regular ocorre numa cadeia de caracteres.

## Sintaxe de Analyze

```python
func.regexp_count(<str>, <pattern>)
```

## Exemplos de Analyze

```python
func.regexp_count('banana', 'an')

┌───┐
│ 2  │
└───┘
```

## Sintaxe SQL

```sql
REGEXP_COUNT(<str>, <pattern>)
```

## Exemplos SQL

```sql
SELECT REGEXP_COUNT('banana', 'an');

┌───┐
│ 2  │
└───┘
```
