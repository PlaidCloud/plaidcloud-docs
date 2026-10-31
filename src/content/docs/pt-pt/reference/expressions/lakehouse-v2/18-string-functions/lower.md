---
title: LOWER (Lakehouse v2)
description: LOWER — converte uma cadeia em minúsculas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lower.md
---

Converte uma cadeia em minúsculas.

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

## Exemplos SQL

```sql
SELECT LOWER('HELLO');

┌───────┐
│ hello  │
└───────┘
```
