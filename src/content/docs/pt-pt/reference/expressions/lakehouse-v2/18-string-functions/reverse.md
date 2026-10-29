---
title: "REVERSE (Cadeia, Lakehouse v2)"
description: REVERSE — inverte uma cadeia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/reverse.md
---

Inverte uma cadeia.

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

## Exemplos SQL

```sql
SELECT REVERSE('hello');

┌───────┐
│ olleh  │
└───────┘
```
