---
title: ARRAY_POSITION (Lakehouse v2)
description: ARRAY_POSITION — devolve a posição da primeira ocorrência de um elemento (indexação a partir de 1).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/array-position.md
---

Devolve a posição da primeira ocorrência de um elemento (indexação a partir de 1).

## Sintaxe do Analyze

```python
func.array_position([10, 20, 30], 20)
```

## Exemplos do Analyze

```python
func.array_position([10, 20, 30], 20)

┌───┐
│ 2 │
└───┘
```

## Sintaxe SQL

```sql
ARRAY_POSITION([10, 20, 30], 20)
```

## Exemplos SQL

```sql
SELECT ARRAY_POSITION([10, 20, 30], 20);

┌───┐
│ 2 │
└───┘
```
