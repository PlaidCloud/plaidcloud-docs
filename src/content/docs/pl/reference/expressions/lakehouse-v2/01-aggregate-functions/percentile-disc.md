---
title: "PERCENTILE_DISC (Aggregate, Lakehouse v2)"
description: "Użyj funkcji agregującej PERCENTILE_DISC w PlaidCloud Lakehouse. Zwraca najmniejszą wartość, której dystrybuanta jest >= podanego percentyla."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/percentile-disc.md
---

Zwraca najmniejszą wartość, której dystrybuanta jest >= podanego percentyla.

## Składnia Analyze

```python
func.percentile_disc(0.5)
```

## Przykłady Analyze

```python
func.percentile_disc(0.5)

┌───────┐
│ 72000 │
└───────┘
```

## Składnia SQL

```sql
PERCENTILE_DISC(0.5)
```

## Przykłady SQL

```sql
SELECT PERCENTILE_DISC(0.5) WITHIN GROUP (ORDER BY salary) FROM employees;

┌───────┐
│ 72000 │
└───────┘
```
