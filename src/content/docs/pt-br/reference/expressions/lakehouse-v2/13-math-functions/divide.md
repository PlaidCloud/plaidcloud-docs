---
title: DIVIDE (Lakehouse v2)
description: DIVIDE — retorna o resultado da divisão de um número por outro.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/divide.md
---

Retorna o resultado da divisão de um número por outro.

## Sintaxe do Analyze

```python
func.divide(<x>, <y>)
```

## Exemplos do Analyze

```python
func.divide(10, 3)

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```

## Sintaxe SQL

```sql
DIVIDE(<x>, <y>)
```

## Exemplos de SQL

```sql
SELECT DIVIDE(10, 3);

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```
