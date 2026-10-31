---
title: POW (Lakehouse v2)
description: POW — retorna um número elevado à potência de outro número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/pow.md
---

Retorna um número elevado à potência de outro número.

## Sintaxe do Analyze

```python
func.pow(<x>, <y>)
```

## Exemplos do Analyze

```python
func.pow(2, 10)

┌────────┐
│ 1024.0  │
└────────┘
```

## Sintaxe SQL

```sql
POW(<x>, <y>)
```

## Exemplos de SQL

```sql
SELECT POW(2, 10);

┌────────┐
│ 1024.0  │
└────────┘
```
