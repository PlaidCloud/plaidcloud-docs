---
title: RAND() (Lakehouse v1)
description: RAND() — zwraca losową liczbę zmiennoprzecinkową v z zakresu 0 <= v < 1.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/rand.md
---

Zwraca losową liczbę zmiennoprzecinkową v z zakresu 0 &lt;= v &lt; 1.0. Aby uzyskać losową liczbę całkowitą R z zakresu i &lt;= R &lt; j, użyj wyrażenia FLOOR(i + RAND() * (j − i)).

## Składnia Analyze

```python
func.rand()
```

## Przykłady Analyze

```python
func.rand()

┌────────────────────┐
│    func.rand()     │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```

## Składnia SQL

```sql
RAND()
```

## Przykłady SQL

```sql
SELECT RAND();

┌────────────────────┐
│       rand()       │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```
