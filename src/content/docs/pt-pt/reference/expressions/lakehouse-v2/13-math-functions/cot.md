---
title: COT (Lakehouse v2)
description: COT — devolve a cotangente de um número em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cot.md
---

Devolve a cotangente de um número em radianos.

## Sintaxe de Analyze

```python
func.cot(<x>)
```

## Exemplos de Analyze

```python
func.cot(1)

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```

## Sintaxe SQL

```sql
COT(<x>)
```

## Exemplos SQL

```sql
SELECT COT(1);

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```
