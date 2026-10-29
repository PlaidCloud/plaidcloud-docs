---
title: LOCATE (Lakehouse v2)
description: LOCATE — devolve a posição da primeira ocorrência de uma subcadeia numa cadeia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/locate.md
---

Devolve a posição da primeira ocorrência de uma subcadeia numa cadeia.

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

## Exemplos SQL

```sql
SELECT LOCATE('or', 'hello world');

┌───┐
│ 8  │
└───┘
```
