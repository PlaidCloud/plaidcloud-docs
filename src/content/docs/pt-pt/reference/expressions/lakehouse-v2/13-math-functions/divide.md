---
title: DIVIDE (Lakehouse v2)
description: DIVIDE — devolve o resultado da divisão de um número por outro.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/divide.md
---

Devolve o resultado da divisão de um número por outro.

## Sintaxe de Analyze

```python
func.divide(<x>, <y>)
```

## Exemplos de Analyze

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

## Exemplos SQL

```sql
SELECT DIVIDE(10, 3);

┌────────────────────┐
│ 3.3333333333333335  │
└────────────────────┘
```
