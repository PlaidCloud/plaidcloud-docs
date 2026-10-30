---
title: FPOW (Lakehouse v2)
description: FPOW — alias de `POW`. Consulte [POW](../pow/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/fpow.md
---

Alias de `POW`. Consulte [POW](../pow/).

## Sintaxe do Analyze

```python
func.fpow(2, 10)
```

## Exemplos do Analyze

```python
func.fpow(2, 10)

┌────────┐
│ 1024.0 │
└────────┘
```

## Sintaxe SQL

```sql
FPOW(<x>)
```

## Exemplos de SQL

```sql
SELECT FPOW(2, 10);

┌────────┐
│ 1024.0 │
└────────┘
```
