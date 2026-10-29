---
title: VARIANT_TYPEOF (Lakehouse v2)
description: VARIANT_TYPEOF — Retorna o nome do tipo de um valor VARIANT como uma string.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/22-variant-functions/variant-typeof.md
---

Retorna o nome do tipo de um valor VARIANT como uma string.

## Sintaxe do Analyze

```python
func.variant_typeof(<variant>)
```

## Exemplos do Analyze

```python
func.variant_typeof(get_column(table, 'data'))

┌──────────┐
│ 'OBJECT'  │
└──────────┘
```

## Sintaxe SQL

```sql
VARIANT_TYPEOF(<variant>)
```

## Exemplos de SQL

```sql
SELECT VARIANT_TYPEOF(data) FROM events;

┌────────┐
│ OBJECT  │
└────────┘
```
