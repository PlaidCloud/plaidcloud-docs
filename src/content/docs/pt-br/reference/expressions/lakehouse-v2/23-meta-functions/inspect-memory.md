---
title: INSPECT_MEMORY (Lakehouse v2)
description: INSPECT_MEMORY — Retorna informações de uso de memória do nó atual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-memory.md
---

Retorna informações de uso de memória do nó atual.

## Sintaxe do Analyze

```python
func.inspect_memory()
```

## Exemplos do Analyze

```python
func.inspect_memory()

┌───────────────┐
│ (memory info)  │
└───────────────┘
```

## Sintaxe SQL

```sql
INSPECT_MEMORY()
```

## Exemplos de SQL

```sql
SELECT * FROM TABLE(INSPECT_MEMORY());

┌──────────────────┐
│ (memory details)  │
└──────────────────┘
```
