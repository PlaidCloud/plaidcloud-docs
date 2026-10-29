---
title: LOG (Lakehouse v2)
description: LOG — retorna o logaritmo de um número em uma base especificada.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log.md
---

Retorna o logaritmo de um número em uma base especificada.

## Sintaxe do Analyze

```python
func.log(<base>, <x>)
```

## Exemplos do Analyze

```python
func.log(10, 100)

┌─────┐
│ 2.0  │
└─────┘
```

## Sintaxe SQL

```sql
LOG(<base>, <x>)
```

## Exemplos de SQL

```sql
SELECT LOG(10, 100);

┌─────┐
│ 2.0  │
└─────┘
```
