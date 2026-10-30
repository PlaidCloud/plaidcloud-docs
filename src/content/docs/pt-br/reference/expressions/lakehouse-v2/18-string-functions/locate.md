---
title: LOCATE (Lakehouse v2)
description: LOCATE — retorna a posição da primeira ocorrência de uma substring em uma string.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/locate.md
---

Retorna a posição da primeira ocorrência de uma substring em uma string.

## Sintaxe do Analyze

```python
func.locate(<substr>, <str>[, <pos>])
```

## Exemplos do Analyze

```python
func.locate('or', 'hello world')

┌───┐
│ 8  │
└───┘
```

## Sintaxe SQL

```sql
LOCATE(<substr>, <str>[, <pos>])
```

## Exemplos de SQL

```sql
SELECT LOCATE('or', 'hello world');

┌───┐
│ 8  │
└───┘
```
