---
title: FIELD (Lakehouse v2)
description: FIELD — devolve a posição de índice de um valor numa lista de argumentos.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/field.md
---

Devolve a posição de índice de um valor numa lista de argumentos.

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

## Exemplos SQL

```sql
SELECT FIELD('b', 'a', 'b', 'c');

┌───┐
│ 2  │
└───┘
```
