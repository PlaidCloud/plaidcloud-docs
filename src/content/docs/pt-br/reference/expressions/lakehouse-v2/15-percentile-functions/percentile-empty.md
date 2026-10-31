---
title: PERCENTILE_EMPTY (Lakehouse v2)
description: PERCENTILE_EMPTY — retorna um estado de percentil vazio para inicialização.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/15-percentile-functions/percentile-empty.md
---

Retorna um estado de percentil vazio para inicialização.

## Sintaxe do Analyze

```python
func.percentile_empty()
```

## Exemplos do Analyze

```python
func.percentile_empty()

┌───────────────┐
│ (empty state)  │
└───────────────┘
```

## Sintaxe SQL

```sql
PERCENTILE_EMPTY()
```

## Exemplos de SQL

```sql
SELECT PERCENTILE_EMPTY();

┌────────────────────┐
│ (percentile state)  │
└────────────────────┘
```
