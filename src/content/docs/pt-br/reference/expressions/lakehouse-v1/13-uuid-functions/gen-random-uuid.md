---
title: GEN_RANDOM_UUID (Lakehouse v1)
description: GEN_RANDOM_UUID — gera um UUID aleatório baseado na v4.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/13-uuid-functions/gen-random-uuid.md
---

Gera um UUID aleatório baseado na v4.

## Sintaxe no Analyze

```python
func.gen_random_uuid()
```

## Exemplos de SQL

```python
func.gen_random_uuid()

┌───────────────────────────────────────┐
│           func.gen_random_uuid()      │
├───────────────────────────────────────|
│ f88e7efe-1bc2-494b-806b-3ffe90db8f47  │
└───────────────────────────────────────┘
```

## Sintaxe SQL

```sql
GEN_RANDOM_UUID()
```

## Aliases

- [UUID](../uuid)

## Exemplos de SQL

```sql
SELECT GEN_RANDOM_UUID(), UUID();

┌─────────────────────────────────────────────────────────────────────────────┐
│           gen_random_uuid()          │                uuid()                │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ f88e7efe-1bc2-494b-806b-3ffe90db8f47 │ f88e7efe-1bc2-494b-806b-3ffe90db8f47 │
└─────────────────────────────────────────────────────────────────────────────┘
```
