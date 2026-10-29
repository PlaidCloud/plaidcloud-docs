---
title: STARTS_WITH (Lakehouse v2)
description: STARTS_WITH — verifica se uma cadeia começa com um prefixo especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/starts-with.md
---

Verifica se uma cadeia começa com um prefixo especificado.

## Sintaxe do Analyze

```python
func.starts_with(<str>, <prefix>)
```

## Exemplos do Analyze

```python
func.starts_with('StarRocks', 'Star')

┌───┐
│ 1  │
└───┘
```

## Sintaxe SQL

```sql
STARTS_WITH(<str>, <prefix>)
```

## Exemplos SQL

```sql
SELECT STARTS_WITH('StarRocks', 'Star');

┌───┐
│ 1  │
└───┘
```
