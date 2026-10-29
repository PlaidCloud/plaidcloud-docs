---
title: SM3 (Lakehouse v2)
description: SM3 — retorna o hash SM3 de uma string.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/sm3.md
---

Retorna o hash SM3 de uma string.

## Sintaxe do Analyze

```python
func.sm3(<str>)
```

## Exemplos do Analyze

```python
func.sm3('hello')

┌───────────────┐
│ 'becbbfaa...'  │
└───────────────┘
```

## Sintaxe SQL

```sql
SM3(<str>)
```

## Exemplos SQL

```sql
SELECT SM3('hello');

┌──────────────────────────────────────────────────────────────────┐
│ becbbfaae6548b8bf0cfcad5a27183cd1be6093b1cceccc303d9c61d0a645268  │
└──────────────────────────────────────────────────────────────────┘
```
