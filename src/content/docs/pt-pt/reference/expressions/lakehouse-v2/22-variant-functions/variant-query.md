---
title: VARIANT_QUERY (Lakehouse v2)
description: "Utilize a função de variant VARIANT_QUERY no PlaidCloud Lakehouse. Consulta um valor de um objeto VARIANT com uma expressão de caminho e devolve um VARIANT."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-query.md
---

Consulta um valor de um objeto VARIANT com uma expressão de caminho e devolve um VARIANT.

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

## Exemplos SQL

```sql
SELECT VARIANT_QUERY(data, '$.address.city') FROM events;

┌────────────┐
│ "New York"  │
└────────────┘
```
