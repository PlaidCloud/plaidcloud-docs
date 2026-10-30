---
title: LIKE (Lakehouse v2)
description: "Utilize a função de correspondência de padrões LIKE no PlaidCloud Lakehouse. Compara uma cadeia de caracteres com um padrão através dos carateres universais `%` (quaisquer carateres) e `_` (um único caráter)."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/14-pattern-matching-functions/like.md
---

Compara uma cadeia de caracteres com um padrão através dos carateres universais `%` (quaisquer carateres) e `_` (um único caráter).

## Sintaxe de Analyze

```python
func.like(<str> LIKE <pattern>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT name FROM users WHERE name LIKE '%alice%';

┌─────────────┐
│ alice_smith  │
└─────────────┘
```
