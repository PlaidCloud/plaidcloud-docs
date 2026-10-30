---
title: INITCAP (Lakehouse v2)
description: INITCAP — converte em maiúscula a primeira letra de cada palavra de uma cadeia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/initcap.md
---

Converte em maiúscula a primeira letra de cada palavra de uma cadeia.

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

## Exemplos SQL

```sql
SELECT INITCAP('hello world');

┌─────────────┐
│ Hello World  │
└─────────────┘
```
