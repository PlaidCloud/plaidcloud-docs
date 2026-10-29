---
title: NOW（Lakehouse v1）
description: NOW — 現在の日付と時刻を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/now.md
---

現在の日付と時刻を返します。

## Analyze 構文

```python
func.now()
```

## Analyze の例

```python
┌─────────────────────────────────────────────────────────┐
│  func.current_timestamp()  │         func.now()         │
├────────────────────────────┼────────────────────────────┤
│ 2024-01-29 04:38:12.584359 │ 2024-01-29 04:38:12.584417 │
└─────────────────────────────────────────────────────────┘
```

## SQL 構文

```sql
NOW()
```

## 戻り値の型

TIMESTAMP

## エイリアス

- [CURRENT_TIMESTAMP](../current-timestamp)

## SQL の例

次の例では、現在の日付と時刻を返します。

```sql
SELECT CURRENT_TIMESTAMP(), NOW();

┌─────────────────────────────────────────────────────────┐
│     current_timestamp()    │            now()           │
├────────────────────────────┼────────────────────────────┤
│ 2024-01-29 04:38:12.584359 │ 2024-01-29 04:38:12.584417 │
└─────────────────────────────────────────────────────────┘
```
