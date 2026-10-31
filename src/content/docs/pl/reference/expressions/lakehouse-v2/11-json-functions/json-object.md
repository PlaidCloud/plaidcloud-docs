---
title: JSON_OBJECT (Lakehouse v2)
description: JSON_OBJECT — tworzy obiekt JSON z par klucz-wartość.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-object.md
---

Tworzy obiekt JSON z par klucz-wartość.

## Składnia Analyze

```python
func.json_object('name', 'Alice', 'age', 30)
```

## Przykłady Analyze

```python
func.json_object('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## Składnia SQL

```sql
JSON_OBJECT('name', 'Alice', 'age', 30)
```

## Przykłady SQL

```sql
SELECT JSON_OBJECT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
