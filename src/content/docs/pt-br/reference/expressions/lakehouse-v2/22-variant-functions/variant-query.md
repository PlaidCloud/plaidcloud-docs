---
title: VARIANT_QUERY (Lakehouse v2)
description: "Use a função variant VARIANT_QUERY no PlaidCloud Lakehouse. Consulta um valor de um objeto VARIANT usando uma expressão de caminho e retorna um VARIANT."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-query.md
---

Consulta um valor de um objeto VARIANT usando uma expressão de caminho e retorna um VARIANT.

## Sintaxe do Analyze

```python
func.variant_query(<variant>, <path>)
```

## Exemplos do Analyze

```python
func.variant_query(get_column(table, 'data'), '$.address.city')

┌──────────────┐
│ '"New York"'  │
└──────────────┘
```

## Sintaxe SQL

```sql
VARIANT_QUERY(<variant>, <path>)
```

## Exemplos de SQL

```sql
SELECT VARIANT_QUERY(data, '$.address.city') FROM events;

┌────────────┐
│ "New York"  │
└────────────┘
```
