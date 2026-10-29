---
title: LOG10 (Lakehouse v2)
description: LOG10 — retorna o logaritmo de base 10 de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log10.md
---

Retorna o logaritmo de base 10 de um número.

## Sintaxe do Analyze

```python
func.log10(<x>)
```

## Exemplos do Analyze

```python
func.log10(1000)

┌─────┐
│ 3.0  │
└─────┘
```

## Sintaxe SQL

```sql
LOG10(<x>)
```

## Exemplos de SQL

```sql
SELECT LOG10(1000);

┌─────┐
│ 3.0  │
└─────┘
```
