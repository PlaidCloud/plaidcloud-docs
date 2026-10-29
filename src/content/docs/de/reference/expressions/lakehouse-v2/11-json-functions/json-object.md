---
title: JSON_OBJECT (Lakehouse v2)
description: JSON_OBJECT – erstellt ein JSON-Objekt aus Schlüssel-Wert-Paaren.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-object.md
---

Erstellt ein JSON-Objekt aus Schlüssel-Wert-Paaren.

## Analyze-Syntax

```python
func.json_object('name', 'Alice', 'age', 30)
```

## Analyze-Beispiele

```python
func.json_object('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## SQL-Syntax

```sql
JSON_OBJECT('name', 'Alice', 'age', 30)
```

## SQL-Beispiele

```sql
SELECT JSON_OBJECT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
