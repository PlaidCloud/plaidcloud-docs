---
title: PMOD (Lakehouse v2)
description: PMOD — devolve o módulo positivo da divisão de dois números.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/pmod.md
---

Devolve o módulo positivo da divisão de dois números.

## Sintaxe de Analyze

```python
func.pmod(<x>, <y>)
```

## Exemplos de Analyze

```python
func.pmod(-10, 3)

┌───┐
│ 2  │
└───┘
```

## Sintaxe SQL

```sql
PMOD(<x>, <y>)
```

## Exemplos SQL

```sql
SELECT PMOD(-10, 3);

┌───┐
│ 2  │
└───┘
```
