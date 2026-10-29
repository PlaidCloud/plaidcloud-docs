---
title: TO_MILLISECONDS (Lakehouse v1)
description: TO_MILLISECONDS — 指定したミリ秒数を Interval 型に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-milliseconds.md
---

指定したミリ秒数を Interval 型に変換します。

- 入力には、正の整数、ゼロ、負の整数を指定できます。

## Analyze の構文

```python
func.to_milliseconds(<milliseconds>)
```

## Analyze の例

```python
func.to_milliseconds(2)
┌──────────────────────────────────────────────────────┐
│ func.to_milliseconds(2)                              │
├──────────────────────────────────────────────────────┤
│  0:00:00.002                                         │
└──────────────────────────────────────────────────────┘
```

## SQL構文

```sql
TO_MILLISECONDS(<milliseconds>)
```

## 戻り値の型

Interval（`hh:mm:ss.sss` 形式）。

## SQLの例

```sql
SELECT TO_MILLISECONDS(2), TO_MILLISECONDS(0), TO_MILLISECONDS((- 2));

┌────────────────────────────────────────────────────────────────┐
│ to_milliseconds(2) │ to_milliseconds(0) │ to_milliseconds(- 2) │
├────────────────────┼────────────────────┼──────────────────────┤
│ 0:00:00.002        │ 00:00:00           │ -0:00:00.002         │
└────────────────────────────────────────────────────────────────┘
```
