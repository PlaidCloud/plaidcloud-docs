---
title: JSON_ARRAY (Lakehouse v2)
description: JSON_ARRAY — cria uma matriz JSON a partir de uma lista de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-array.md
---

Cria uma matriz JSON a partir de uma lista de valores.

## Sintaxe de Analyze

```python
func.json_array(1, 'hello', None)
```

## Exemplos de Analyze

```python
func.json_array(1, 'hello', None)

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```

## Sintaxe SQL

```sql
JSON_ARRAY(1, 'hello', None)
```

## Exemplos SQL

```sql
SELECT JSON_ARRAY(1, 'hello', NULL);

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```
