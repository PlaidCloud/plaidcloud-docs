---
title: ATAN2 (Lakehouse v2)
description: ATAN2 — devolve o arco tangente de y/x, utilizando os sinais para determinar o quadrante.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/atan2.md
---

Devolve o arco tangente de y/x, utilizando os sinais para determinar o quadrante.

## Sintaxe de Analyze

```python
func.atan2(<y>, <x>)
```

## Exemplos de Analyze

```python
func.atan2(1, 1)

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```

## Sintaxe SQL

```sql
ATAN2(<y>, <x>)
```

## Exemplos SQL

```sql
SELECT ATAN2(1, 1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```
