---
title: CONCAT_WS (Lakehouse v2)
description: CONCAT_WS：使用分隔符连接字符串。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/concat-ws.md
---

使用分隔符连接字符串。

## Analyze 语法

```python
func.concat_ws(<sep>, <str1>, <str2>[, ...])
```

## Analyze 示例

```python
func.concat_ws('-', '2024', '01', '15')

┌──────────────┐
│ '2024-01-15'  │
└──────────────┘
```

## SQL 语法

```sql
CONCAT_WS(<sep>, <str1>, <str2>[, ...])
```

## SQL 示例

```sql
SELECT CONCAT_WS('-', '2024', '01', '15');

┌────────────┐
│ 2024-01-15  │
└────────────┘
```
