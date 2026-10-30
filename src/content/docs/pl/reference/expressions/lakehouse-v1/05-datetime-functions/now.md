---
title: NOW (Lakehouse v1)
description: NOW — zwraca bieżącą datę i godzinę.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/now.md
---

Zwraca bieżącą datę i godzinę.

## Składnia Analyze

```python
func.now()
```

## Przykłady Analyze

```python
┌─────────────────────────────────────────────────────────┐
│  func.current_timestamp()  │         func.now()         │
├────────────────────────────┼────────────────────────────┤
│ 2024-01-29 04:38:12.584359 │ 2024-01-29 04:38:12.584417 │
└─────────────────────────────────────────────────────────┘
```

## Składnia SQL

```sql
NOW()
```

## Zwracany typ

TIMESTAMP

## Aliasy

- [CURRENT_TIMESTAMP](../current-timestamp)

## Przykłady SQL

Ten przykład zwraca bieżącą datę i godzinę:

```sql
SELECT CURRENT_TIMESTAMP(), NOW();

┌─────────────────────────────────────────────────────────┐
│     current_timestamp()    │            now()           │
├────────────────────────────┼────────────────────────────┤
│ 2024-01-29 04:38:12.584359 │ 2024-01-29 04:38:12.584417 │
└─────────────────────────────────────────────────────────┘
```
