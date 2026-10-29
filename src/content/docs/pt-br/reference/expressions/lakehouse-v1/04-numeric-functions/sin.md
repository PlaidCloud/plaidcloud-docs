---
title: SIN (Lakehouse v1)
description: SIN — retorna o seno de x, em que x é dado em radianos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/sin.md
---

Retorna o seno de `x`, em que `x` é dado em radianos.

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

## Exemplos de SQL

```sql
SELECT SIN(90);

┌────────────────────┐
│       sin(90)      │
├────────────────────┤
│ 0.8939966636005579 │
└────────────────────┘
```
