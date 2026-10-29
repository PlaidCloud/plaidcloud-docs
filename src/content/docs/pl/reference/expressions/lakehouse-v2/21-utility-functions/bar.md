---
title: BAR (Lakehouse v2)
description: "Użyj funkcji narzędziowej BAR w PlaidCloud Lakehouse. Zwraca wizualną reprezentację wartości w postaci paska tekstowego w zadanym zakresie. Przydatna w wizualizacjach tekstowych."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/bar.md
---

Zwraca wizualną reprezentację wartości w postaci paska tekstowego w zadanym zakresie. Przydatna w wizualizacjach tekstowych.

## Składnia Analyze

```python
func.bar(<value>, <min>, <max>, <width>)
```

## Przykłady Analyze

```python
func.bar(50, 0, 100, 20)

┌──────────────────────┐
│ ██████████           │
└──────────────────────┘
```

## Składnia SQL

```sql
BAR(<value>, <min>, <max>, <width>)
```

## Przykłady SQL

```sql
SELECT score, BAR(score, 0, 100, 20) AS bar FROM students;

┌───────┬──────────────────────┐
│ score │ bar                  │
├───────┼──────────────────────┤
│    25 │ █████                │
│    50 │ ██████████           │
│    75 │ ███████████████      │
│   100 │ ████████████████████ │
└───────┴──────────────────────┘
```
