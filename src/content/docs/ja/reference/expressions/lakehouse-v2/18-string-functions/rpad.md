---
title: RPAD（Lakehouse v2）
description: RPAD — 指定した長さになるまで、文字列の右側を埋め込み文字列でパディングします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/rpad.md
---

指定した長さになるまで、文字列の右側を埋め込み文字列でパディングします。

## Analyze 構文

```python
func.rpad(<str>, <len>, <pad>)
```

## Analyze の例

```python
func.rpad('hello', 10, '.')

┌──────────────┐
│ 'hello.....'  │
└──────────────┘
```

## SQL 構文

```sql
RPAD(<str>, <len>, <pad>)
```

## SQL の例

```sql
SELECT RPAD('hello', 10, '.');

┌────────────┐
│ hello.....  │
└────────────┘
```
