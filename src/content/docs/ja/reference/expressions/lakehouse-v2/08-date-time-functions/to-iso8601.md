---
title: TO_ISO8601 (Lakehouse v2)
description: TO_ISO8601 — 日付または日時を ISO 8601 形式の文字列に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/to-iso8601.md
---

日付または日時を ISO 8601 形式の文字列に変換します。

## Analyzeの構文

```python
func.to_iso8601(<datetime>)
```

## Analyzeの例

```python
func.to_iso8601('2024-06-15 14:30:00')

┌───────────────────────┐
│ '2024-06-15T14:30:00'  │
└───────────────────────┘
```

## SQLの構文

```sql
TO_ISO8601(<datetime>)
```

## SQLの例

```sql
SELECT TO_ISO8601('2024-06-15 14:30:00');

┌─────────────────────┐
│ 2024-06-15T14:30:00  │
└─────────────────────┘
```
