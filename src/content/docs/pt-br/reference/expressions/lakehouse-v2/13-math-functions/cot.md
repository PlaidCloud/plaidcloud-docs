---
title: COT (Lakehouse v2)
description: COT — retorna a cotangente de um número em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/cot.md
---

Retorna a cotangente de um número em radianos.

## Sintaxe do Analyze

```python
func.cot(<x>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT COT(1);

┌────────────────────┐
│ 0.6420926159343306  │
└────────────────────┘
```
