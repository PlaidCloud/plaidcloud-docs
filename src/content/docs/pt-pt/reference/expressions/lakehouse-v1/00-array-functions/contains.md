---
title: CONTAINS (Lakehouse v1)
description: CONTAINS — verifica se a matriz contém um elemento específico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/contains.md
---

Verifica se a matriz contém um elemento específico.


## Sintaxe do Analyze

```python
func.contains( <array>, <element> )
```

## Exemplos do Analyze

```python
func.contains([1, 2], 1)

┌───────────────────────────┐
│ func.contains([1, 2], 1)  │
├───────────────────────────┤
│ true                      │
└───────────────────────────┘
```

## Sintaxe SQL

```sql
CONTAINS( <array>, <element> )
```

## Alias

- [ARRAY_CONTAINS](../array-contains)

## Exemplos SQL

```sql
SELECT ARRAY_CONTAINS([1, 2], 1), CONTAINS([1, 2], 1);

┌─────────────────────────────────────────────────┐
│ array_contains([1, 2], 1) │ contains([1, 2], 1) │
├───────────────────────────┼─────────────────────┤
│ true                      │ true                │
└─────────────────────────────────────────────────┘
```
