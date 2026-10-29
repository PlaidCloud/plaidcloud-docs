---
title: JSON_OBJECT (Lakehouse v2)
description: JSON_OBJECT — cria um objeto JSON a partir de pares chave-valor.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/11-json-functions/json-object.md
---

Cria um objeto JSON a partir de pares chave-valor.

## Sintaxe do Analyze

```python
func.json_object('name', 'Alice', 'age', 30)
```

## Exemplos do Analyze

```python
func.json_object('name', 'Alice', 'age', 30)

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```

## Sintaxe SQL

```sql
JSON_OBJECT('name', 'Alice', 'age', 30)
```

## Exemplos de SQL

```sql
SELECT JSON_OBJECT('name', 'Alice', 'age', 30);

┌───────────────────────────┐
│ {"name":"Alice","age":30} │
└───────────────────────────┘
```
