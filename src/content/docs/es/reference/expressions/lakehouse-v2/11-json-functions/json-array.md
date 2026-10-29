---
title: JSON_ARRAY (Lakehouse v2)
description: JSON_ARRAY — crea una matriz JSON a partir de una lista de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-array.md
---

Crea una matriz JSON a partir de una lista de valores.

## Sintaxis de Analyze

```python
func.json_array(1, 'hello', None)
```

## Ejemplos de Analyze

```python
func.json_array(1, 'hello', None)

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```

## Sintaxis de SQL

```sql
JSON_ARRAY(1, 'hello', None)
```

## Ejemplos de SQL

```sql
SELECT JSON_ARRAY(1, 'hello', NULL);

┌──────────────────┐
│ [1,"hello",null] │
└──────────────────┘
```
