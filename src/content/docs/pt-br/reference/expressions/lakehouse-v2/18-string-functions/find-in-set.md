---
title: FIND_IN_SET (Lakehouse v2)
description: FIND_IN_SET — retorna a posição de uma string em uma lista separada por vírgulas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/find-in-set.md
---

Retorna a posição de uma string em uma lista separada por vírgulas.

## Sintaxe do Analyze

```python
func.find_in_set(<str>, <strlist>)
```

## Exemplos do Analyze

```python
func.find_in_set('b', 'a,b,c')

┌───┐
│ 2  │
└───┘
```

## Sintaxe SQL

```sql
FIND_IN_SET(<str>, <strlist>)
```

## Exemplos de SQL

```sql
SELECT FIND_IN_SET('b', 'a,b,c');

┌───┐
│ 2  │
└───┘
```
