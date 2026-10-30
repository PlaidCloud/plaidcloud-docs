---
title: GREATEST (Lakehouse v1)
description: GREATEST — retorna o valor máximo de um conjunto de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/greatest.md
---

Retorna o valor máximo de um conjunto de valores.

## Sintaxe do Analyze

```python
func.greatest(<value1>, <value2> ...)
```

## Exemplos do Analyze

```python
func.greatest((5, 9, 4))

┌──────────────────────────┐
│ func.greatest((5, 9, 4)) │
├──────────────────────────┤
│                        9 │
└──────────────────────────┘
```

## Sintaxe SQL

```sql
GREATEST(<value1>, <value2> ...)
```

## Exemplos de SQL

```sql
SELECT GREATEST(5, 9, 4);

┌───────────────────┐
│ greatest(5, 9, 4) │
├───────────────────┤
│                 9 │
└───────────────────┘
```
