---
title: TAN (Lakehouse v1)
description: TAN — retorna a tangente de x, em que x é dado em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/tan.md
---

Retorna a tangente de `x`, em que `x` é dado em radianos.

## Sintaxe do Analyze

```python
func.tan( <x> )
```

## Exemplos do Analyze

```python
func.tan(90)

┌────────────────────┐
│    func.tan(90)    │
├────────────────────┤
│ -1.995200412208242 │
└────────────────────┘
```

## Sintaxe SQL

```sql
TAN( <x> )
```

## Exemplos de SQL

```sql
SELECT TAN(90);

┌────────────────────┐
│       tan(90)      │
├────────────────────┤
│ -1.995200412208242 │
└────────────────────┘
```
