---
title: ATAN (Lakehouse v2)
description: ATAN — retorna o arco tangente de um número em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/atan.md
---

Retorna o arco tangente de um número em radianos.

## Sintaxe do Analyze

```python
func.atan(<x>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT ATAN(1);

┌────────────────────┐
│ 0.7853981633974483  │
└────────────────────┘
```
