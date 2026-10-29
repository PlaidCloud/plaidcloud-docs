---
title: UUID_V7（Lakehouse v2）
description: UUID_V7 — 時間順に並ぶ UUID v7 の文字列を返します。UUID v7 の値は作成時刻でソートできます。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-v7.md
---

時間順に並ぶ UUID v7 の文字列を返します。UUID v7 の値は作成時刻でソートできます。

## Analyze 構文

```python
func.uuid_v7()
```

## Analyze の例

```python
func.uuid_v7()

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```

## SQL 構文

```sql
UUID_V7()
```

## SQL の例

```sql
SELECT UUID_V7();

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```
