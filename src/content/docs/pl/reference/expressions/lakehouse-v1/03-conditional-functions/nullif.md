---
title: NULLIF (Lakehouse v1)
description: NULLIF — zwraca NULL, jeśli dwa wyrażenia są równe.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/nullif.md
---

Zwraca NULL, jeśli dwa wyrażenia są równe. W przeciwnym razie zwraca expr1. Muszą mieć ten sam typ danych.

## Składnia Analyze

```python
func.nullif(<expr1>, <expr2>)
```

## Przykłady Analyze

```python
func.nullif(0, null) 

┌──────────────────────┐
│ func.nullif(0, null) │
├──────────────────────┤
│                    0 │
└──────────────────────┘
```

## Składnia SQL

```sql
NULLIF(<expr1>, <expr2>)
```

## Przykłady SQL

```sql
SELECT NULLIF(0, NULL);

┌─────────────────┐
│ nullif(0, null) │
├─────────────────┤
│               0 │
└─────────────────┘
```
