---
title: ENDS_WITH (Lakehouse v2)
description: ENDS_WITH — Verifica se uma string termina com um sufixo especificado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ends-with.md
---

Verifica se uma string termina com um sufixo especificado.

## Sintaxe do Analyze

```python
func.ends_with(<str>, <suffix>)
```

## Exemplos do Analyze

```python
func.ends_with('hello world', 'world')

┌───┐
│ 1  │
└───┘
```

## Sintaxe SQL

```sql
ENDS_WITH(<str>, <suffix>)
```

## Exemplos de SQL

```sql
SELECT ENDS_WITH('hello world', 'world');

┌───┐
│ 1  │
└───┘
```
