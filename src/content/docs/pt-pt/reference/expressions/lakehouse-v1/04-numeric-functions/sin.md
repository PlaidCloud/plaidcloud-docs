---
title: SIN (Lakehouse v1)
description: SIN — devolve o seno de x, em que x é dado em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sin.md
---

Devolve o seno de `x`, em que `x` é dado em radianos.

## Sintaxe do Analyze

```python
func.sin( <x> )
```

## Exemplos do Analyze

```python
func.sin(90)

┌────────────────────┐
│    func.sin(90)    │
├────────────────────┤
│ 0.8939966636005579 │
└────────────────────┘
```

## Sintaxe SQL

```sql
SIN( <x> )
```

## Exemplos SQL

```sql
SELECT SIN(90);

┌────────────────────┐
│       sin(90)      │
├────────────────────┤
│ 0.8939966636005579 │
└────────────────────┘
```
