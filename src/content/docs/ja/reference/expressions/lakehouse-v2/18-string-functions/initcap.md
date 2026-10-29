---
title: INITCAP（Lakehouse v2）
description: INITCAP — 文字列内の各単語の先頭文字を大文字にします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/initcap.md
---

文字列内の各単語の先頭文字を大文字にします。

## Analyze 構文

```python
func.initcap(<str>)
```

## Analyze の例

```python
func.initcap('hello world')

┌───────────────┐
│ 'Hello World'  │
└───────────────┘
```

## SQL 構文

```sql
INITCAP(<str>)
```

## SQL の例

```sql
SELECT INITCAP('hello world');

┌─────────────┐
│ Hello World  │
└─────────────┘
```
