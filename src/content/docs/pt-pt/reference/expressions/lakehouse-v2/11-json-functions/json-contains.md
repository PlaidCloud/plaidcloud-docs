---
title: JSON_CONTAINS (Lakehouse v2)
description: JSON_CONTAINS — verifica se um documento JSON contém um valor específico num caminho.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-contains.md
---

Verifica se um documento JSON contém um valor específico num caminho.

## Sintaxe de Analyze

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')
```

## Exemplos de Analyze

```python
func.json_contains(get_column(table, 'data'), '"Alice"', '$.name')

┌───┐
│ 1 │
└───┘
```

## Sintaxe SQL

```sql
JSON_CONTAINS(<data>, '"Alice"', '$.name')
```

## Exemplos SQL

```sql
SELECT JSON_CONTAINS('{"name":"Alice"}', '"Alice"', '$.name');

┌───┐
│ 1 │
└───┘
```
