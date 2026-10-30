---
title: TOMORROW (Lakehouse v1)
description: TOMORROW — 明日の日付を返します。today() + 1 と同じです。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/tomorrow.md
---

明日の日付を返します。`today() + 1` と同じです。

## Analyze の構文

```python
func.tomorrow()
```

## Analyze の例

```python
func.tomorrow()
┌─────────────────┐
│ func.tomorrow() │
├─────────────────┤
│ 2021-09-03      │
└─────────────────┘
```

## SQL構文

```sql
TOMORROW()
```

## 戻り値の型

`DATE`。「YYYY-MM-DD」形式の日付を返します。

## SQLの例

```sql
SELECT TOMORROW();
┌────────────┐
│ TOMORROW() │
├────────────┤
│ 2021-09-04 │
└────────────┘

SELECT TODAY()+1;
┌───────────────┐
│ (TODAY() + 1) │
├───────────────┤
│ 2021-09-04    │
└───────────────┘
```
