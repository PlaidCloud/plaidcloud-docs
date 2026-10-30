---
title: LEAST (Lakehouse v1)
description: LEAST — devolve o valor mínimo de um conjunto de valores.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/least.md
---

Devolve o valor mínimo de um conjunto de valores.

## Sintaxe do Analyze

```python
func.least((<value1>, <value2> ...))
```

## Exemplos do Analyze

```python
func.least((5, 9, 4))

┌───────────────────────┐
│ func.least((5, 9, 4)) │
├───────────────────────┤
│                     4 │
└───────────────────────┘
```

## Sintaxe SQL

```sql
LEAST(<value1>, <value2> ...)
```

## Exemplos SQL

```sql
SELECT LEAST(5, 9, 4);

┌────────────────┐
│ least(5, 9, 4) │
├────────────────┤
│              4 │
└────────────────┘
```
