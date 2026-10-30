---
title: SPLIT_PART (Lakehouse v2)
description: SPLIT_PART — divide uma cadeia por um delimitador e devolve o elemento num índice especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/split-part.md
---

Divide uma cadeia por um delimitador e devolve o elemento num índice especificado.

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

## Exemplos SQL

```sql
SELECT SPLIT_PART('a-b-c', '-', 2);

┌───┐
│ b  │
└───┘
```
