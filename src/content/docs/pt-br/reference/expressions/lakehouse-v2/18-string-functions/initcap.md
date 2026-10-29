---
title: INITCAP (Lakehouse v2)
description: INITCAP — Coloca em maiúscula a primeira letra de cada palavra de uma string.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/initcap.md
---

Coloca em maiúscula a primeira letra de cada palavra de uma string.

## Sintaxe do Analyze

```python
func.initcap(<str>)
```

## Exemplos do Analyze

```python
func.initcap('hello world')

┌───────────────┐
│ 'Hello World'  │
└───────────────┘
```

## Sintaxe SQL

```sql
INITCAP(<str>)
```

## Exemplos de SQL

```sql
SELECT INITCAP('hello world');

┌─────────────┐
│ Hello World  │
└─────────────┘
```
