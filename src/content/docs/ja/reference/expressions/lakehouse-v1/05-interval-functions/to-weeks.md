---
title: TO_WEEKS (Lakehouse v1)
description: TO_WEEKS — 指定した週数を Interval 型に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-weeks.md
---

指定した週数を Interval 型に変換します。

- 入力には、正の整数、ゼロ、負の整数を指定できます。

## Analyze の構文

```python
func.to_weeks(<weeks>)
```

## Analyze の例

```python
func.to_weeks(2)
┌──────────────────────────────────────────────────────┐
│ func.to_weeks(2)                                     │
├──────────────────────────────────────────────────────┤
│ 14 days                                              │
└──────────────────────────────────────────────────────┘
```

## SQL構文

```sql
TO_WEEKS(<weeks>)
```

## 戻り値の型

Interval（日で表されます）。

## SQLの例

```sql
SELECT TO_WEEKS(2), TO_WEEKS(0), TO_WEEKS((- 2));

┌───────────────────────────────────────────┐
│ to_weeks(2) │ to_weeks(0) │ to_weeks(- 2) │
├─────────────┼─────────────┼───────────────┤
│ 14 days     │ 00:00:00    │ -14 days      │
└───────────────────────────────────────────┘
```
