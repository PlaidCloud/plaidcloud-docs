---
title: ACOS (Lakehouse v2)
description: ACOS — devolve o arco cosseno de um número em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/acos.md
---

Devolve o arco cosseno de um número em radianos.

## Sintaxe de Analyze

```python
func.acos(<x>)
```

## Exemplos de Analyze

```python
func.acos(0.5)

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```

## Sintaxe SQL

```sql
ACOS(<x>)
```

## Exemplos SQL

```sql
SELECT ACOS(0.5);

┌────────────────────┐
│ 1.0471975511965976  │
└────────────────────┘
```
