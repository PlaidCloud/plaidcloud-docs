---
title: TIMESTAMP_DIFF（Lakehouse v1）
description: TIMESTAMP_DIFF — 2 つのタイムスタンプの差を計算し、INTERVAL として返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/timestamp-diff.md
---

2 つのタイムスタンプの差を計算し、INTERVAL として返します。

## Analyze 構文

```python
func.timestamp_diff(<timestamp1>, <timestamp2>)
```

## Analyze の例

```python
func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))
┌────────────────────────────────────────────────────────────────────────────────────────┐
│ func.timestamp_diff(func.to_timestamp('2025-02-01'), func.to_timestamp('2025-01-01'))  │
├────────────────────────────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                                              │
└────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 構文

```sql
TIMESTAMP_DIFF(<timestamp1>, <timestamp2>)
```

## 戻り値の型

INTERVAL（`hours:minutes:seconds` 形式）。

## SQL の例

次の例は、2025 年 2 月 1 日と 2025 年 1 月 1 日の時間差が 744 時間（31 日に相当）であることを示しています。

```sql
SELECT TIMESTAMP_DIFF('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP);

┌──────────────────────────────────────────────────────────────────┐
│ timestamp_diff('2025-02-01'::TIMESTAMP, '2025-01-01'::TIMESTAMP) │
├──────────────────────────────────────────────────────────────────┤
│ 744:00:00                                                        │
└──────────────────────────────────────────────────────────────────┘
```
