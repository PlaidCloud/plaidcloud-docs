---
title: UNIX_TIMESTAMP (Lakehouse v2)
description: UNIX_TIMESTAMP — 日時をUnixタイムスタンプに変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/unix-timestamp.md
---

日時をUnixタイムスタンプに変換します。

## Analyzeの構文

```python
func.unix_timestamp([<datetime>])
```

## Analyzeの例

```python
func.unix_timestamp('2024-01-01 00:00:00')

┌────────────┐
│ 1704067200  │
└────────────┘
```

## SQLの構文

```sql
UNIX_TIMESTAMP([<datetime>])
```

## SQLの例

```sql
SELECT UNIX_TIMESTAMP('2024-01-01 00:00:00');

┌────────────┐
│ 1704067200  │
└────────────┘
```
