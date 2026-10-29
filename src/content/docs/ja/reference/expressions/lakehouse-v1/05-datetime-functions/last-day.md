---
title: LAST_DAY（Lakehouse v1）
description: LAST_DAY — 指定した間隔（週、月、四半期、または年）の最終日を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/last-day.md
---

指定した日付またはタイムスタンプに基づいて、指定した間隔（週、月、四半期、または年）の最終日を返します。

## Analyze 構文

```python
func.last_day(<date_expression>, <interval>)
```

## Analyze の例

```python
func.last_day(func.to_date('2024-11-13'), 'month')
┌──────────────────────────────────────────────────────┐
│ func.last_day(func.to_date('2024-11-13'), 'month')   │
├──────────────────────────────────────────────────────┤
│ 2024-11-30                                           │
└──────────────────────────────────────────────────────┘
```

## SQL 構文

```sql
LAST_DAY(<date_expression>, <interval>)
```

| パラメーター           | 説明                                                                                                   |
|---------------------|---------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | 指定した間隔の最終日を計算する対象の DATE または TIMESTAMP の値です。                                |
| `<interval>`        | 最終日を求める間隔の種類です。指定できる値は `week`、`month`、`quarter`、`year` です。 |

## 戻り値の型

日付。

## SQL の例

取引の任意の日付（例：2024-11-13）に基づいて、常に月末である請求日を求めるとします。

```sql
SELECT LAST_DAY(to_date('2024-11-13'), month) AS billing_date;

┌──────────────┐
│ billing_date │
├──────────────┤
│ 2024-11-30   │
└──────────────┘
```
