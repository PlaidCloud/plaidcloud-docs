---
title: TAN (Lakehouse v2)
description: TAN — devolve a tangente de um número em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/tan.md
---

Devolve a tangente de um número em radianos.

## Sintaxe de Analyze

```python
func.tan(<x>)
```

## Exemplos de Analyze

```python
func.tan(0)

┌─────┐
│ 0.0  │
└─────┘
```

## Sintaxe SQL

```sql
TAN(<x>)
```

## Exemplos SQL

```sql
SELECT TAN(0);

┌─────┐
│ 0.0  │
└─────┘
```
