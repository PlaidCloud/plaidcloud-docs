---
title: SIGN (Lakehouse v2)
description: "SIGN — retorna o sinal de um número: -1, 0 ou 1."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/sign.md
---

Retorna o sinal de um número: -1, 0 ou 1.

## Sintaxe do Analyze

```python
func.sign(<x>)
```

## Exemplos do Analyze

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

## Exemplos de SQL

```sql
SELECT SIGN(-42);

┌────┐
│ -1  │
└────┘
```
