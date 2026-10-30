---
title: LENGTH (Lakehouse v2)
description: LENGTH — retorna o comprimento de uma string em bytes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/length.md
---

Retorna o comprimento de uma string em bytes.

## Sintaxe do Analyze

```python
func.length(<str>)
```

## Exemplos do Analyze

```python
func.length('hello')

┌───┐
│ 5  │
└───┘
```

## Sintaxe SQL

```sql
LENGTH(<str>)
```

## Exemplos de SQL

```sql
SELECT LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
