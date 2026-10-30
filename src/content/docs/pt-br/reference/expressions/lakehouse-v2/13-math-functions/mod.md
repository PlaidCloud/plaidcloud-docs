---
title: MOD (Lakehouse v2)
description: MOD — retorna o resto da divisão de dois números.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/mod.md
---

Retorna o resto da divisão de dois números.

## Sintaxe do Analyze

```python
func.mod(<x>, <y>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT MOD(10, 3);

┌───┐
│ 1  │
└───┘
```
