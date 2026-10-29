---
title: GEN_RANDOM_UUID (Lakehouse v1)
description: GEN_RANDOM_UUID — generuje losowy identyfikator UUID w wersji 4.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/13-uuid-functions/gen-random-uuid.md
---

Generuje losowy identyfikator UUID w wersji 4.

## Składnia Analyze

```python
func.gen_random_uuid()
```

## Przykłady SQL

```python
func.gen_random_uuid()

┌───────────────────────────────────────┐
│           func.gen_random_uuid()      │
├───────────────────────────────────────|
│ f88e7efe-1bc2-494b-806b-3ffe90db8f47  │
└───────────────────────────────────────┘
```

## Składnia SQL

```sql
GEN_RANDOM_UUID()
```

## Aliasy

- [UUID](../uuid)

## Przykłady SQL

```sql
SELECT GEN_RANDOM_UUID(), UUID();

┌─────────────────────────────────────────────────────────────────────────────┐
│           gen_random_uuid()          │                uuid()                │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ f88e7efe-1bc2-494b-806b-3ffe90db8f47 │ f88e7efe-1bc2-494b-806b-3ffe90db8f47 │
└─────────────────────────────────────────────────────────────────────────────┘
```
