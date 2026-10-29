---
title: VARIANT_GET (Lakehouse v2)
description: VARIANT_GET — extrait une valeur typée d'un objet VARIANT à un chemin donné.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-get.md
---

Extrait une valeur typée d'un objet VARIANT à un chemin donné.

## Syntaxe Analyze

```python
func.variant_get(<variant>, <path>, <type>)
```

## Exemples Analyze

```python
func.variant_get(get_column(table, 'data'), '$.name', 'STRING')

┌─────────┐
│ 'Alice'  │
└─────────┘
```

## Syntaxe SQL

```sql
VARIANT_GET(<variant>, <path>, <type>)
```

## Exemples SQL

```sql
SELECT VARIANT_GET(data, '$.name', 'STRING') FROM events;

┌───────┐
│ Alice  │
└───────┘
```
