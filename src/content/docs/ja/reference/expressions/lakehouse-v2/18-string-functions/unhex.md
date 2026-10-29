---
title: UNHEX（Lakehouse v2）
description: UNHEX — 16進数文字列を文字列に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/unhex.md
---

16進数文字列を文字列に変換します。

## Analyze 構文

```python
func.unhex(<hex_str>)
```

## Analyze の例

```python
func.unhex('48656C6C6F')

┌─────────┐
│ 'Hello'  │
└─────────┘
```

## SQL 構文

```sql
UNHEX(<hex_str>)
```

## SQL の例

```sql
SELECT UNHEX('48656C6C6F');

┌───────┐
│ Hello  │
└───────┘
```
