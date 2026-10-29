---
title: VARIANT_QUERY (Lakehouse v2)
description: "Utilisez la fonction variant VARIANT_QUERY dans PlaidCloud Lakehouse. Interroge une valeur d'un objet VARIANT à l'aide d'une expression de chemin et renvoie un VARIANT."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-query.md
---

Interroge une valeur d'un objet VARIANT à l'aide d'une expression de chemin et renvoie un VARIANT.

## Syntaxe Analyze

```python
func.variant_query(<variant>, <path>)
```

## Exemples Analyze

```python
func.variant_query(get_column(table, 'data'), '$.address.city')

┌──────────────┐
│ '"New York"'  │
└──────────────┘
```

## Syntaxe SQL

```sql
VARIANT_QUERY(<variant>, <path>)
```

## Exemples SQL

```sql
SELECT VARIANT_QUERY(data, '$.address.city') FROM events;

┌────────────┐
│ "New York"  │
└────────────┘
```
