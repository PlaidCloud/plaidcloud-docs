---
title: TO_MONTHS (Lakehouse v1)
description: TO_MONTHS — 指定した月数を Interval 型に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-months.md
---

指定した月数を Interval 型に変換します。

- 入力には、正の整数、ゼロ、負の整数を指定できます。

## Analyze の構文

```python
func.to_months(<months>)
```

## Analyze の例

```python
func.to_months(2)
┌──────────────────────────────────────────────────────┐
│ func.to_months(2)                                    │
├──────────────────────────────────────────────────────┤
│ 2 months                                             │
└──────────────────────────────────────────────────────┘
```

## SQL構文

```sql
TO_MONTHS(<months>)
```

## 戻り値の型

Interval（月で表されます）。

## SQLの例

```sql
SELECT TO_MONTHS(2), TO_MONTHS(0), TO_MONTHS((- 2));

┌──────────────────────────────────────────────┐
│ to_months(2) │ to_months(0) │ to_months(- 2) │
├──────────────┼──────────────┼────────────────┤
│ 2 months     │ 00:00:00     │ -2 months      │
└──────────────────────────────────────────────┘
```
