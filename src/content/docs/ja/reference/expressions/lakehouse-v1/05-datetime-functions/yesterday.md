---
title: YESTERDAY (Lakehouse v1)
description: YESTERDAY — 昨日の日付を返します。today() - 1 と同じです。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/yesterday.md
---

昨日の日付を返します。`today() - 1` と同じです。

## Analyze の構文

```python
func.yesterday()
```

## Analyze の例

```python
func.yesterday()
┌──────────────────┐
│ func.yesterday() │
├──────────────────┤
│ 2021-09-02       │
└──────────────────┘
```

## SQL構文

```sql
YESTERDAY()
```

## 戻り値の型

`DATE`。「YYYY-MM-DD」形式の日付を返します。

## SQLの例

```sql
SELECT YESTERDAY();
┌─────────────┐
│ YESTERDAY() │
├─────────────┤
│ 2021-09-02  │
└─────────────┘

SELECT TODAY()-1;
┌───────────────┐
│ (TODAY() - 1) │
├───────────────┤
│ 2021-09-02    │
└───────────────┘
```
