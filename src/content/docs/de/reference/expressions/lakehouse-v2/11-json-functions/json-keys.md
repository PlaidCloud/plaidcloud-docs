---
title: JSON_KEYS (Lakehouse v2)
description: JSON_KEYS – gibt die Schlüssel des JSON-Objekts der obersten Ebene als JSON-Array zurück.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-keys.md
---

Gibt die Schlüssel des JSON-Objekts der obersten Ebene als JSON-Array zurück.

## Analyze-Syntax

```python
func.json_keys(get_column(table, 'data'))
```

## Analyze-Beispiele

```python
func.json_keys(get_column(table, 'data'))

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```

## SQL-Syntax

```sql
JSON_KEYS(<data>)
```

## SQL-Beispiele

```sql
SELECT JSON_KEYS(PARSE_JSON('{"name":"Alice","age":30}'));

┌────────────────┐
│ ["name","age"] │
└────────────────┘
```
