---
title: "REVERSE (String, Lakehouse v2)"
description: REVERSE — inverte uma string.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/reverse.md
---

Inverte uma string.

## Sintaxe do Analyze

```python
func.reverse(<str>)
```

## Exemplos do Analyze

```python
func.reverse('hello')

┌─────────┐
│ 'olleh'  │
└─────────┘
```

## Sintaxe SQL

```sql
REVERSE(<str>)
```

## Exemplos de SQL

```sql
SELECT REVERSE('hello');

┌───────┐
│ olleh  │
└───────┘
```
