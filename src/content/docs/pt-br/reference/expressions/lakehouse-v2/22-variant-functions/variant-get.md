---
title: VARIANT_GET (Lakehouse v2)
description: VARIANT_GET — extrai um valor tipado de um objeto VARIANT em um caminho especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-get.md
---

Extrai um valor tipado de um objeto VARIANT em um caminho especificado.

## Sintaxe do Analyze

```python
func.variant_get(<variant>, <path>, <type>)
```

## Exemplos do Analyze

```python
func.variant_get(get_column(table, 'data'), '$.name', 'STRING')

┌─────────┐
│ 'Alice'  │
└─────────┘
```

## Sintaxe SQL

```sql
VARIANT_GET(<variant>, <path>, <type>)
```

## Exemplos de SQL

```sql
SELECT VARIANT_GET(data, '$.name', 'STRING') FROM events;

┌───────┐
│ Alice  │
└───────┘
```
