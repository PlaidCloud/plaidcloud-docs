---
title: RAND(n) (Lakehouse v1)
description: RAND(n) — zwraca losową liczbę zmiennoprzecinkową v z zakresu 0 &lt;= v &lt; 1.0.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/randn.md
---

Zwraca losową liczbę zmiennoprzecinkową v z zakresu 0 &lt;= v &lt; 1.0. Aby uzyskać losową liczbę całkowitą R z zakresu i &lt;= R &lt; j, użyj wyrażenia FLOOR(i + RAND() * (j − i)). Argument `n` służy jako ziarno. Dla takich samych wartości argumentu RAND(n) zawsze zwraca tę samą wartość, dzięki czemu tworzy powtarzalną sekwencję wartości w kolumnie.

## Składnia Analyze

```python
func.rand( <n>)
```

## Przykłady Analyze

```python
func.rand(1)

┌────────────────────┐
│    func.rand(1)    │
├────────────────────┤
│ 0.7133693869548766 │
└────────────────────┘
```

## Składnia SQL

```sql
RAND( <n>)
```

## Przykłady SQL

```sql
SELECT RAND(1);

┌────────────────────┐
│       rand(1)      │
├────────────────────┤
│ 0.7133693869548766 │
└────────────────────┘
```
