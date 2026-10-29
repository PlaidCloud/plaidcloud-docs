---
title: DATABASE (Lakehouse v2)
description: DATABASE — retorna o nome do banco de dados atual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/database.md
---

Retorna o nome do banco de dados atual.

## Sintaxe do Analyze

```python
func.database()
```

## Exemplos do Analyze

```python
func.database()

┌───────────────┐
│ 'my_database'  │
└───────────────┘
```

## Sintaxe SQL

```sql
DATABASE()
```

## Exemplos de SQL

```sql
SELECT DATABASE();

┌─────────────┐
│ my_database  │
└─────────────┘
```
