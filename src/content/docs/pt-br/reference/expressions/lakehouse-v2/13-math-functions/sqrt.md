---
title: SQRT (Lakehouse v2)
description: SQRT — retorna a raiz quadrada de um número.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sqrt.md
---

Retorna a raiz quadrada de um número.

## Sintaxe do Analyze

```python
func.sqrt(<x>)
```

## Exemplos do Analyze

```python
func.sqrt(144)

┌──────┐
│ 12.0  │
└──────┘
```

## Sintaxe SQL

```sql
SQRT(<x>)
```

## Exemplos de SQL

```sql
SELECT SQRT(144);

┌──────┐
│ 12.0  │
└──────┘
```
