---
title: TIMEZONE（Lakehouse v1）
description: TIMEZONE — 現在の接続のタイムゾーンを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/timezone.md
---

現在の接続のタイムゾーンを返します。 

PlaidCloud Lakehouse は、デフォルトのタイムゾーンとして UTC（協定世界時）を使用します。タイムゾーンは、お客様の現在の地理的な位置に合わせて変更できます。`timezone` 設定に割り当てられる値については、https://docs.rs/chrono-tz/latest/chrono_tz/enum.Tz.html を参照してください。詳細は次の例をご覧ください。

## Analyze 構文

```python
func.timezone()
```

## Analyze の例

```python
func.timezone()
┌─────────────────────┐
│ timezone            │
├─────────────────────┤
│ UTC                 │
└─────────────────────┘
```

## SQL 構文

```sql
SELECT TIMEZONE();
```

## SQL の例

```sql
-- Return the current timezone
SELECT TIMEZONE();
┌─────────────────┐
│ TIMEZONE('UTC') │
├─────────────────┤
│ UTC             │
└─────────────────┘

-- Set the timezone to China Standard Time
SET timezone='Asia/Shanghai';

SELECT TIMEZONE();
┌───────────────────────────┐
│ TIMEZONE('Asia/Shanghai') │
├───────────────────────────┤
│ Asia/Shanghai             │
└───────────────────────────┘
```
