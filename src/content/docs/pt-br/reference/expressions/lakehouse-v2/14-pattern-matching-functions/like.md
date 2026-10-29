---
title: LIKE (Lakehouse v2)
description: "Use a função de correspondência de padrões LIKE no PlaidCloud Lakehouse. Compara uma string com um padrão usando `%` (quaisquer caracteres) e `_` (um único caractere)."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/like.md
---

Compara uma string com um padrão usando os curingas `%` (quaisquer caracteres) e `_` (um único caractere).

## Sintaxe do Analyze

```python
func.like(<str> LIKE <pattern>)
```

## Exemplos do Analyze

```python
get_column(table, 'name').like('%alice%')

┌───────────┐
│ (boolean)  │
└───────────┘
```

## Sintaxe SQL

```sql
LIKE(<str> LIKE <pattern>)
```

## Exemplos de SQL

```sql
SELECT name FROM users WHERE name LIKE '%alice%';

┌─────────────┐
│ alice_smith  │
└─────────────┘
```
