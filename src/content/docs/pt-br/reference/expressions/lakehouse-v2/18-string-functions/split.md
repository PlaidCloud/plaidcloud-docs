---
title: SPLIT (Lakehouse v2)
description: SPLIT — divide uma string por um delimitador e retorna um array.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/split.md
---

Divide uma string por um delimitador e retorna um array.

## Sintaxe do Analyze

```python
func.split(<str>, <delimiter>)
```

## Exemplos do Analyze

```python
func.split('a,b,c', ',')

┌───────────────┐
│ ['a','b','c']  │
└───────────────┘
```

## Sintaxe SQL

```sql
SPLIT(<str>, <delimiter>)
```

## Exemplos de SQL

```sql
SELECT SPLIT('a,b,c', ',');

┌───────────────┐
│ ["a","b","c"]  │
└───────────────┘
```
