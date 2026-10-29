---
title: UUID_V7_NUMERIC（Lakehouse v2）
description: UUID_V7_NUMERIC — 時間順に並ぶ UUID v7 を128ビットの LARGEINT 値として返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-v7-numeric.md
---

時間順に並ぶ UUID v7 を128ビットの LARGEINT 値として返します。UUID v7 の値は作成時刻でソートできます。

## Analyze 構文

```python
func.uuid_v7_numeric()
```

## Analyze の例

```python
func.uuid_v7_numeric()

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```

## SQL 構文

```sql
UUID_V7_NUMERIC()
```

## SQL の例

```sql
SELECT UUID_V7_NUMERIC();

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```
