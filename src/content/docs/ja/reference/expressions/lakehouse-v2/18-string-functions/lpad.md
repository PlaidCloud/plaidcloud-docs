---
title: LPAD（Lakehouse v2）
description: LPAD — 指定した長さになるまで、文字列の左側を埋め込み文字列でパディングします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/lpad.md
---

指定した長さになるまで、文字列の左側を埋め込み文字列でパディングします。

## Analyze 構文

```python
func.lpad(<str>, <len>, <pad>)
```

## Analyze の例

```python
func.lpad('42', 5, '0')

┌─────────┐
│ '00042'  │
└─────────┘
```

## SQL 構文

```sql
LPAD(<str>, <len>, <pad>)
```

## SQL の例

```sql
SELECT LPAD('42', 5, '0');

┌───────┐
│ 00042  │
└───────┘
```
