---
title: QUOTE（Lakehouse v1）
description: QUOTE——对字符串加引号，生成可在 SQL 语句中用作正确转义数据值的结果。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/quote.md
---

对字符串加引号，生成可在 SQL 语句中用作正确转义数据值的结果。

## Analyze 语法

```python
func.quote(<str>)
```

## Analyze 示例

```python
func.quote('Don\'t')
┌──────────────────────┐
│ func.quote('Don\'t') │
├──────────────────────┤
│  Don\'t!             │
└──────────────────────┘
```

## SQL 语法

```sql
QUOTE(<str>)
```

## SQL 示例

```sql
SELECT QUOTE('Don\'t!');
┌─────────────────┐
│ QUOTE('Don't!') │
├─────────────────┤
│ Don\'t!         │
└─────────────────┘

SELECT QUOTE(NULL);
┌─────────────┐
│ QUOTE(NULL) │
├─────────────┤
│        NULL │
└─────────────┘
```
