---
title: UPPER (Lakehouse v2)
description: UPPER — converte uma string para maiúsculas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/upper.md
---

Converte uma string para maiúsculas.

## Sintaxe do Analyze

```python
func.upper(<str>)
```

## Exemplos do Analyze

```python
func.upper('hello')

┌─────────┐
│ 'HELLO'  │
└─────────┘
```

## Sintaxe SQL

```sql
UPPER(<str>)
```

## Exemplos de SQL

```sql
SELECT UPPER('hello');

┌───────┐
│ HELLO  │
└───────┘
```
