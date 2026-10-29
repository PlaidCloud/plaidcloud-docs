---
title: ATAN (Lakehouse v2)
description: ATAN — devolve o arco tangente de um número em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/atan.md
---

Devolve o arco tangente de um número em radianos.

## Sintaxe de Analyze

```python
func.atan(<x>)
```

## Exemplos de Analyze

```python
func.atan(1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## Sintaxe SQL

```sql
ATAN(<x>)
```

## Exemplos SQL

```sql
SELECT ATAN(1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```
