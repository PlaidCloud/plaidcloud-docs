---
title: JSON_OBJECT (Lakehouse v2)
description: JSON_OBJECT — crea un objeto JSON a partir de pares clave-valor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-object.md
---

Crea un objeto JSON a partir de pares clave-valor.

## Sintaxis de Analyze

```python
func.json_object('name', 'Alice', 'age', 30)
```

## Ejemplos de Analyze

```python
func.json_object('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## Sintaxis de SQL

```sql
JSON_OBJECT('name', 'Alice', 'age', 30)
```

## Ejemplos de SQL

```sql
SELECT JSON_OBJECT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
