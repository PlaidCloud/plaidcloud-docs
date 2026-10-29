---
title: CONNECTION_ID (Lakehouse v1)
description: CONNECTION_ID — zwraca identyfikator bieżącego połączenia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/connection-id.md
---

Zwraca identyfikator bieżącego połączenia.

## Składnia Analyze

```python
func.connection_id()
```

## Przykłady Analyze

```python
func.connection_id()

┌──────────────────────────────────────┐
│       func.connection_id()           │
├──────────────────────────────────────┤
│ 23cb06ec-583e-4eba-b790-7c8cf72a53f8 │
└──────────────────────────────────────┘
```

## Składnia SQL

```sql
CONNECTION_ID()
```

## Przykłady SQL

```sql
SELECT CONNECTION_ID();

┌──────────────────────────────────────┐
│            connection_id()           │
├──────────────────────────────────────┤
│ 23cb06ec-583e-4eba-b790-7c8cf72a53f8 │
└──────────────────────────────────────┘
```
