---
title: LEAST (Lakehouse v2)
description: LEAST — retorna o menor valor de uma lista de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/least.md
---

Retorna o menor valor de uma lista de valores.

## Sintaxe do Analyze

```python
func.least(<val1>, <val2>[, ...])
```

## Exemplos do Analyze

```python
func.least(3, 7, 1, 9, 4)

┌───┐
│ 1  │
└───┘
```

## Sintaxe SQL

```sql
LEAST(<val1>, <val2>[, ...])
```

## Exemplos de SQL

```sql
SELECT LEAST(3, 7, 1, 9, 4);

┌───┐
│ 1  │
└───┘
```
