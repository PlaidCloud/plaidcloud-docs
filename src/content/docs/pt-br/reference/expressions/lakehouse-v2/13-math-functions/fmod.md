---
title: FMOD (Lakehouse v2)
description: FMOD — retorna o resto de ponto flutuante da divisão de dois números.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/fmod.md
---

Retorna o resto de ponto flutuante da divisão de dois números.

## Sintaxe do Analyze

```python
func.fmod(<x>, <y>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT FMOD(10.5, 3.0);

┌─────┐
│ 1.5  │
└─────┘
```
