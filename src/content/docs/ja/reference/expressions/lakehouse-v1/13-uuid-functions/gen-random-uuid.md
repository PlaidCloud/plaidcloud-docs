---
title: GEN_RANDOM_UUID（Lakehouse v1）
description: GEN_RANDOM_UUID — v4に基づくランダムなUUIDを生成します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/13-uuid-functions/gen-random-uuid.md
---

v4に基づくランダムなUUIDを生成します。

## Analyzeの構文

```python
func.gen_random_uuid()
```

## SQLの例

```python
func.gen_random_uuid()

┌───────────────────────────────────────┐
│           func.gen_random_uuid()      │
├───────────────────────────────────────|
│ f88e7efe-1bc2-494b-806b-3ffe90db8f47  │
└───────────────────────────────────────┘
```

## SQLの構文

```sql
GEN_RANDOM_UUID()
```

## エイリアス

- [UUID](../uuid)

## SQLの例

```sql
SELECT GEN_RANDOM_UUID(), UUID();

┌─────────────────────────────────────────────────────────────────────────────┐
│           gen_random_uuid()          │                uuid()                │
├──────────────────────────────────────┼──────────────────────────────────────┤
│ f88e7efe-1bc2-494b-806b-3ffe90db8f47 │ f88e7efe-1bc2-494b-806b-3ffe90db8f47 │
└─────────────────────────────────────────────────────────────────────────────┘
```
