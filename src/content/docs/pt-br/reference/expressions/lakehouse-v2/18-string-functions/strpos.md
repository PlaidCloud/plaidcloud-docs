---
title: STRPOS (Lakehouse v2)
description: STRPOS — retorna a posição da primeira ocorrência de uma substring. Alias de `LOCATE`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strpos.md
---

Retorna a posição da primeira ocorrência de uma substring. Alias de `LOCATE`.

## Sintaxe do Analyze

```python
func.strpos(<str>, <substr>)
```

## Exemplos do Analyze

```python
func.strpos('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## Sintaxe SQL

```sql
STRPOS(<str>, <substr>)
```

## Exemplos de SQL

```sql
SELECT STRPOS('hello world', 'world');

┌───┐
│ 7  │
└───┘
```
