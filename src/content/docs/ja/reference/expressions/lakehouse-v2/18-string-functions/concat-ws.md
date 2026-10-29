---
title: CONCAT_WS（Lakehouse v2）
description: CONCAT_WS — 区切り文字を使って文字列を連結します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/concat-ws.md
---

区切り文字を使って文字列を連結します。

## Analyze 構文

```python
func.concat_ws(<sep>, <str1>, <str2>[, ...])
```

## Analyze の例

```python
func.concat_ws('-', '2024', '01', '15')

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## SQL 構文

```sql
CONCAT_WS(<sep>, <str1>, <str2>[, ...])
```

## SQL の例

```sql
SELECT CONCAT_WS('-', '2024', '01', '15');

┌────────────┐
│ 2024-01-15  │
└────────────┘
```
