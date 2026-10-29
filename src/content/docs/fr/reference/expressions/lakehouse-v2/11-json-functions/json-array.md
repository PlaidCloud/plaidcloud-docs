---
title: JSON_ARRAY (Lakehouse v2)
description: JSON_ARRAY — crée un tableau JSON à partir d'une liste de valeurs.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-array.md
---

Crée un tableau JSON à partir d'une liste de valeurs.

## Syntaxe Analyze

```python
func.json_array(1, 'hello', None)
```

## Exemples Analyze

```python
func.json_array(1, 'hello', None)

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```

## Syntaxe SQL

```sql
JSON_ARRAY(1, 'hello', None)
```

## Exemples SQL

```sql
SELECT JSON_ARRAY(1, 'hello', NULL);

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```
