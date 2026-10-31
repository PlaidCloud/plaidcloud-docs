---
title: DCEIL (Lakehouse v2)
description: DCEIL — alias funkcji `CEIL`. Zobacz [CEIL](../ceil/).
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/dceil.md
---

Alias funkcji `CEIL`. Zobacz [CEIL](../ceil/).

## Składnia Analyze

```python
func.dceil(3.2)
```

## Przykłady Analyze

```python
func.dceil(3.2)

┌───┐
│ 4 │
└───┘
```

## Składnia SQL

```sql
DCEIL(<x>)
```

## Przykłady SQL

```sql
SELECT DCEIL(3.2);

┌───┐
│ 4 │
└───┘
```
