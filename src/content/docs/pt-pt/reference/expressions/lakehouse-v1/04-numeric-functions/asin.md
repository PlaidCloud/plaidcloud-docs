---
title: ASIN (Lakehouse v1)
description: ASIN — devolve o arco seno de x, ou seja, o valor cujo seno é x.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/asin.md
---

Devolve o arco seno de `x`, ou seja, o valor cujo seno é `x`. Devolve NULL se `x` não estiver no intervalo de -1 a 1.

## Sintaxe do Analyze

```python
func.asin( <x> )
```

## Exemplos do Analyze

```python
func.asin(0.2)

┌────────────────────┐
│   func.asin(0.2)   │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```

## Sintaxe SQL

```sql
ASIN( <x> )
```

## Exemplos SQL

```sql
SELECT ASIN(0.2);

┌────────────────────┐
│      asin(0.2)     │
├────────────────────┤
│ 0.2013579207903308 │
└────────────────────┘
```
