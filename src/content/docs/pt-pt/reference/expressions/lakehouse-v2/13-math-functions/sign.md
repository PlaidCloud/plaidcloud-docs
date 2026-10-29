---
title: SIGN (Lakehouse v2)
description: "SIGN — devolve o sinal de um número: -1, 0 ou 1."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sign.md
---

Devolve o sinal de um número: -1, 0 ou 1.

## Sintaxe de Analyze

```python
func.sign(<x>)
```

## Exemplos de Analyze

```python
func.sign(-42)

┌────┐
│ -1  │
└────┘
```

## Sintaxe SQL

```sql
SIGN(<x>)
```

## Exemplos SQL

```sql
SELECT SIGN(-42);

┌────┐
│ -1  │
└────┘
```
