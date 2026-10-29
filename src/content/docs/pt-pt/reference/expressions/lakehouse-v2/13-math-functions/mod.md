---
title: MOD (Lakehouse v2)
description: MOD — devolve o resto da divisão de dois números.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/mod.md
---

Devolve o resto da divisão de dois números.

## Sintaxe de Analyze

```python
func.mod(<x>, <y>)
```

## Exemplos de Analyze

```python
func.mod(10, 3)

┌───┐
│ 1  │
└───┘
```

## Sintaxe SQL

```sql
MOD(<x>, <y>)
```

## Exemplos SQL

```sql
SELECT MOD(10, 3);

┌───┐
│ 1  │
└───┘
```
