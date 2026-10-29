---
title: PARSE_JSON (Lakehouse v2)
description: PARSE_JSON — analyse une chaîne JSON et renvoie une valeur JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/parse-json.md
---

Analyse une chaîne JSON et renvoie une valeur JSON.

## Syntaxe Analyze

```python
func.parse_json('{"a":1}')
```

## Exemples Analyze

```python
func.parse_json('{"a": 1}')

┌─────────────┐
│ JSON object │
└─────────────┘
```

## Syntaxe SQL

```sql
PARSE_JSON('{"a":1}')
```

## Exemples SQL

```sql
SELECT PARSE_JSON('{"name": "Alice"}');

┌──────────────────┐
│ {"name":"Alice"} │
└──────────────────┘
```
