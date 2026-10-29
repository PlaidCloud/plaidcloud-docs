---
title: SPLIT_PART (Lakehouse v2)
description: SPLIT_PART — divide uma string por um delimitador e retorna o elemento em um índice especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/split-part.md
---

Divide uma string por um delimitador e retorna o elemento em um índice especificado.

## Sintaxe do Analyze

```python
func.split_part(<str>, <delimiter>, <index>)
```

## Exemplos do Analyze

```python
func.split_part('a-b-c', '-', 2)

┌─────┐
│ 'b'  │
└─────┘
```

## Sintaxe SQL

```sql
SPLIT_PART(<str>, <delimiter>, <index>)
```

## Exemplos de SQL

```sql
SELECT SPLIT_PART('a-b-c', '-', 2);

┌───┐
│ b  │
└───┘
```
