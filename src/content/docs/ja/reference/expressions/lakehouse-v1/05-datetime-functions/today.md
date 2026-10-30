---
title: TODAY (Lakehouse v1)
description: TODAY — 現在の日付を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/today.md
---

現在の日付を返します。

## Analyze の構文

```python
func.today()
```

## Analyze の例

```python
func.today()
┌──────────────┐
│ func.today() │
├──────────────┤
│ 2021-09-03   │
└──────────────┘
```

## SQL構文

```sql
TODAY()
```

## 戻り値の型

`DATE`。「YYYY-MM-DD」形式の日付を返します。

## SQLの例

```sql
SELECT TODAY();
┌────────────┐
│ TODAY()    │
├────────────┤
│ 2021-09-03 │
└────────────┘
```
