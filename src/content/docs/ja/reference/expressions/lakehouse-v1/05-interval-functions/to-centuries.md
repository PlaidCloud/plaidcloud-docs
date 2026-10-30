---
title: TO_CENTURIES (Lakehouse v1)
description: TO_CENTURIES — 指定した世紀数を Interval 型に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-centuries.md
---

指定した世紀数を Interval 型に変換します。

- 入力には、正の整数、ゼロ、負の整数を指定できます。

## Analyze の構文

```python
func.to_centuries(<centuries>)
```

## Analyze の例

```python
func.to_centuries(2)
┌──────────────────────────────────────────────────────┐
│ func.to_centuries(2)                                 │
├──────────────────────────────────────────────────────┤
│ 200 years                                            │
└──────────────────────────────────────────────────────┘
```

## SQL構文

```sql
TO_CENTURIES(<centuries>)
```

## 戻り値の型

Interval（年で表されます）。

## SQLの例

```sql
SELECT TO_CENTURIES(2), TO_CENTURIES(0), TO_CENTURIES(-2);

┌───────────────────────────────────────────────────────┐
│ to_centuries(2) │ to_centuries(0) │ to_centuries(- 2) │
├─────────────────┼─────────────────┼───────────────────┤
│ 200 years       │ 00:00:00        │ -200 years        │
└───────────────────────────────────────────────────────┘
```
