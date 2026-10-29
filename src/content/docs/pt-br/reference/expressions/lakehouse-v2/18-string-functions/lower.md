---
title: LOWER (Lakehouse v2)
description: LOWER — converte uma string para minúsculas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lower.md
---

Converte uma string para minúsculas.

## Sintaxe do Analyze

```python
func.lower(<str>)
```

## Exemplos do Analyze

```python
func.lower('HELLO')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Sintaxe SQL

```sql
LOWER(<str>)
```

## Exemplos de SQL

```sql
SELECT LOWER('HELLO');

┌───────┐
│ hello  │
└───────┘
```
