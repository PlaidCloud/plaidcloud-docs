---
title: JSON_REMOVE (Lakehouse v2)
description: JSON_REMOVE — remove um elemento de um documento JSON em um caminho especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-remove.md
---

Remove um elemento de um documento JSON em um caminho especificado.

## Sintaxe do Analyze

```python
func.json_remove(get_column(table, 'data'), '$.temp')
```

## Exemplos do Analyze

```python
func.json_remove(get_column(table, 'data'), '$.temp')

┌──────────────────────┐
│ JSON without element │
└──────────────────────┘
```

## Sintaxe SQL

```sql
JSON_REMOVE(<data>, '$.temp')
```

## Exemplos de SQL

```sql
SELECT JSON_REMOVE(PARSE_JSON('{"name":"Alice","temp":1}'), '$.temp');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
