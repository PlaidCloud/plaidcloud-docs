---
title: ASIN (Lakehouse v2)
description: ASIN — retorna o arco seno de um número em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/asin.md
---

Retorna o arco seno de um número em radianos.

## Sintaxe do Analyze

```python
func.asin(<x>)
```

## Exemplos do Analyze

```python
func.asin(0.5)

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```

## Sintaxe SQL

```sql
ASIN(<x>)
```

## Exemplos de SQL

```sql
SELECT ASIN(0.5);

┌────────────────────┐
│ 0.5235987755982988  │
└────────────────────┘
```
