---
title: NEXT_DAY（Lakehouse v1）
description: NEXT_DAY — 指定した日付またはタイムスタンプより後で、次に来る指定した曜日の日付を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/next-day.md
---

指定した日付またはタイムスタンプより後で、次に来る指定した曜日の日付を返します。

## Analyze 構文

```python
func.next_day(date_expression>, <target_day>)
```

## Analyze の例

```python
func.next_day(func.to_date('2024-11-13'), 'monday')
┌──────────────────────────────────────────────────────┐
│ func.next_day(func.to_date('2024-11-13'), 'monday')  │
├──────────────────────────────────────────────────────┤
│ 2024-11-18                                           │
└──────────────────────────────────────────────────────┘
```

## SQL 構文

```sql
NEXT_DAY(<date_expression>, <target_day>)
```

| パラメーター           | 説明                                                                                                                                                              |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `<date_expression>` | 指定した曜日が次に来る日付を計算する対象の `DATE` または `TIMESTAMP` の値です。                                                                                 |
| `<target_day>`      | 次の該当日を求める対象の曜日です。指定できる値は `monday`、`tuesday`、`wednesday`、`thursday`、`friday`、`saturday`、`sunday` です。 |

## 戻り値の型

日付。

## SQL の例

特定の日付（たとえば 2024-11-13）の次の月曜日を求めるには、次のようにします。

```sql
SELECT NEXT_DAY(to_date('2024-11-13'), monday) AS next_monday;

┌─────────────┐
│ next_monday │
├─────────────┤
│ 2024-11-18  │
└─────────────┘
```
