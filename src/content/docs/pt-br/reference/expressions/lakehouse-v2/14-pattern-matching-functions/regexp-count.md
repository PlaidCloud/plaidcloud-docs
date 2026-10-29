---
title: REGEXP_COUNT (Lakehouse v2)
description: "Use a função de correspondência de padrões REGEXP_COUNT no PlaidCloud Lakehouse. Retorna o número de vezes que um padrão de expressão regular ocorre em uma string."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/regexp-count.md
---

Retorna o número de vezes que um padrão de expressão regular ocorre em uma string.

## Sintaxe do Analyze

```python
func.regexp_count(<str>, <pattern>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT REGEXP_COUNT('banana', 'an');

┌───┐
│ 2  │
└───┘
```
