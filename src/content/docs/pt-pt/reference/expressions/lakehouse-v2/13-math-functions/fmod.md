---
title: FMOD (Lakehouse v2)
description: FMOD — devolve o resto em vírgula flutuante da divisão de dois números.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/fmod.md
---

Devolve o resto em vírgula flutuante da divisão de dois números.

## Sintaxe de Analyze

```python
func.fmod(<x>, <y>)
```

## Exemplos de Analyze

```python
func.fmod(10.5, 3.0)

┌─────┐
│ 1.5  │
└─────┘
```

## Sintaxe SQL

```sql
FMOD(<x>, <y>)
```

## Exemplos SQL

```sql
SELECT FMOD(10.5, 3.0);

┌─────┐
│ 1.5  │
└─────┘
```
