---
title: INSPECT_MEMORY (Lakehouse v2)
description: INSPECT_MEMORY — devolve informação sobre a utilização de memória do nó atual.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-memory.md
---

Devolve informação sobre a utilização de memória do nó atual.

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

## Exemplos SQL

```sql
SELECT * FROM TABLE(INSPECT_MEMORY());

┌──────────────────┐
│ (memory details)  │
└──────────────────┘
```
