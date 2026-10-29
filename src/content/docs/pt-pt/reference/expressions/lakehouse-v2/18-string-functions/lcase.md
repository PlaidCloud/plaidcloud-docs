---
title: LCASE (Lakehouse v2)
description: LCASE — converte uma cadeia em minúsculas. Alias de `LOWER`.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lcase.md
---

Converte uma cadeia em minúsculas. Alias de `LOWER`.

## Sintaxe do Analyze

```python
func.lcase(<str>)
```

## Exemplos do Analyze

```python
func.lcase('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Sintaxe SQL

```sql
LCASE(<str>)
```

## Exemplos SQL

```sql
SELECT LCASE('HELLO');

┌───────┐
│ hello  │
└───────┘
```
