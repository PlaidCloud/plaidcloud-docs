---
title: GEN_RANDOM_UUID (Lakehouse v1)
description: GEN_RANDOM_UUID — génère un UUID aléatoire basé sur la v4.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/13-uuid-functions/gen-random-uuid.md
---

Génère un UUID aléatoire basé sur la v4.

## Syntaxe Analyze

```python
func.gen_random_uuid()
```

## Exemples SQL

```python
func.gen_random_uuid()

┌───────────────────────────────────────┐
│           func.gen_random_uuid()      │
├───────────────────────────────────────|
│ f88e7efe-1bc2-494b-806b-3ffe90db8f47  │
└───────────────────────────────────────┘
```

## Syntaxe SQL

```sql
GEN_RANDOM_UUID()
```

## Alias

- [UUID](../uuid)

## Exemples SQL

```sql
SELECT GEN_RANDOM_UUID(), UUID();

┌─────────────────────────────────────────────────────────────────────────────┐
│           gen_random_uuid()          │                uuid()                │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ f88e7efe-1bc2-494b-806b-3ffe90db8f47 │ f88e7efe-1bc2-494b-806b-3ffe90db8f47 │
└─────────────────────────────────────────────────────────────────────────────┘
```
