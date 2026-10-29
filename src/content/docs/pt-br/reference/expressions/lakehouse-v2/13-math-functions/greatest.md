---
title: GREATEST (Lakehouse v2)
description: GREATEST — retorna o maior valor de uma lista de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/greatest.md
---

Retorna o maior valor de uma lista de valores.

## Sintaxe do Analyze

```python
func.greatest(<val1>, <val2>[, ...])
```

## Exemplos do Analyze

```python
func.greatest(3, 7, 1, 9, 4)

┌───┐
│ 9  │
└───┘
```

## Sintaxe SQL

```sql
GREATEST(<val1>, <val2>[, ...])
```

## Exemplos de SQL

```sql
SELECT GREATEST(3, 7, 1, 9, 4);

┌───┐
│ 9  │
└───┘
```
