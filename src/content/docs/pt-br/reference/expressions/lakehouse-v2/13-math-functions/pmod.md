---
title: PMOD (Lakehouse v2)
description: PMOD — retorna o módulo positivo da divisão de dois números.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/pmod.md
---

Retorna o módulo positivo da divisão de dois números.

## Sintaxe do Analyze

```python
func.pmod(<x>, <y>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT PMOD(-10, 3);

┌───┐
│ 2  │
└───┘
```
