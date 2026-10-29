---
title: "REVERSE（文字列、Lakehouse v2）"
description: REVERSE — 文字列を逆順にします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/reverse.md
---

文字列を逆順にします。

## Analyze 構文

```python
func.reverse(<str>)
```

## Analyze の例

```python
func.reverse('hello')

┌─────────┐
│ 'olleh'  │
└─────────┘
```

## SQL 構文

```sql
REVERSE(<str>)
```

## SQL の例

```sql
SELECT REVERSE('hello');

┌───────┐
│ olleh  │
└───────┘
```
