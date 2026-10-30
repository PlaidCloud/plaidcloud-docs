---
title: REPLACE (Lakehouse v2)
description: REPLACE — Substitui todas as ocorrências de uma substring por outra substring.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/replace.md
---

Substitui todas as ocorrências de uma substring por outra substring.

## Sintaxe do Analyze

```python
func.replace(<str>, <old>, <new>)
```

## Exemplos do Analyze

```python
func.replace('hello world', 'world', 'there')

┌───────────────┐
│ 'hello there'  │
└───────────────┘
```

## Sintaxe SQL

```sql
REPLACE(<str>, <old>, <new>)
```

## Exemplos de SQL

```sql
SELECT REPLACE('hello world', 'world', 'there');

┌─────────────┐
│ hello there  │
└─────────────┘
```
