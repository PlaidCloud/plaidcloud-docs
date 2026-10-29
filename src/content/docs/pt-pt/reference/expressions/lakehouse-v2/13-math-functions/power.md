---
title: POWER (Lakehouse v2)
description: POWER — devolve um número elevado à potência de outro número. Alias de `POW`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/power.md
---

Devolve um número elevado à potência de outro número. Alias de `POW`.

## Sintaxe de Analyze

```python
func.power(<x>, <y>)
```

## Exemplos de Analyze

```python
func.power(2, 10)

┌────────┐
│ 1024.0  │
└────────┘
```

## Sintaxe SQL

```sql
POWER(<x>, <y>)
```

## Exemplos SQL

```sql
SELECT POWER(2, 10);

┌────────┐
│ 1024.0  │
└────────┘
```
