---
title: JSON_OBJECT (Lakehouse v2)
description: JSON_OBJECT — crée un objet JSON à partir de paires clé-valeur.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-object.md
---

Crée un objet JSON à partir de paires clé-valeur.

## Syntaxe Analyze

```python
func.json_object('name', 'Alice', 'age', 30)
```

## Exemples Analyze

```python
func.json_object('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## Syntaxe SQL

```sql
JSON_OBJECT('name', 'Alice', 'age', 30)
```

## Exemples SQL

```sql
SELECT JSON_OBJECT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
