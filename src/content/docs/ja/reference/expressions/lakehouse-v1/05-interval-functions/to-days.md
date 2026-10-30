---
title: TO_DAYS (Lakehouse v1)
description: TO_DAYS — 指定した日数を Interval 型に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-days.md
---

指定した日数を Interval 型に変換します。

- 入力には、正の整数、ゼロ、負の整数を指定できます。

## Analyze の構文

```python
func.to_days(<days>)
```

## Analyze の例

```python
func.to_days(2)
┌──────────────────────────────────────────────────────┐
│ func.to_days(2)                                      │
├──────────────────────────────────────────────────────┤
│ 200 days                                             │
└──────────────────────────────────────────────────────┘
```

## SQL構文

```sql
TO_DAYS(<days>)
```

## 戻り値の型

Interval（日で表されます）。

## SQLの例

```sql
SELECT TO_DAYS(2), TO_DAYS(0), TO_DAYS(-2);

┌────────────────────────────────────────┐
│ to_days(2) │ to_days(0) │ to_days(- 2) │
├────────────┼────────────┼──────────────┤
│ 2 days     │ 00:00:00   │ -2 days      │
└────────────────────────────────────────┘
```
