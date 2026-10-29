---
title: INSPECT_MEMORY_DETAIL (Lakehouse v2)
description: INSPECT_MEMORY_DETAIL — Retorna informações detalhadas de uso de memória.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-memory-detail.md
---

Retorna informações detalhadas de uso de memória.

## Sintaxe do Analyze

```python
func.inspect_memory_detail()
```

## Exemplos do Analyze

```python
func.inspect_memory_detail()

┌──────────┐
│ (detail)  │
└──────────┘
```

## Sintaxe SQL

```sql
INSPECT_MEMORY_DETAIL()
```

## Exemplos de SQL

```sql
SELECT * FROM TABLE(INSPECT_MEMORY_DETAIL());

┌─────────────────┐
│ (memory detail)  │
└─────────────────┘
```
