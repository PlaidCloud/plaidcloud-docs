---
title: LENGTH (Lakehouse v2)
description: LENGTH — devolve o comprimento de uma cadeia em bytes.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/length.md
---

Devolve o comprimento de uma cadeia em bytes.

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

## Exemplos SQL

```sql
SELECT LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
