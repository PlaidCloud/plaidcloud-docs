---
title: FIELD (Lakehouse v2)
description: FIELD — Retorna a posição de índice de um valor em uma lista de argumentos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/field.md
---

Retorna a posição de índice de um valor em uma lista de argumentos.

## Sintaxe do Analyze

```python
func.field(<str>, <val1>, <val2>[, ...])
```

## Exemplos do Analyze

```python
func.field('b', 'a', 'b', 'c')

┌───┐
│ 2  │
└───┘
```

## Sintaxe SQL

```sql
FIELD(<str>, <val1>, <val2>[, ...])
```

## Exemplos de SQL

```sql
SELECT FIELD('b', 'a', 'b', 'c');

┌───┐
│ 2  │
└───┘
```
