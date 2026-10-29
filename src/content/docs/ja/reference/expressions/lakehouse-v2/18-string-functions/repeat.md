---
title: REPEAT（Lakehouse v2）
description: REPEAT — 文字列を指定した回数だけ繰り返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/repeat.md
---

文字列を指定した回数だけ繰り返します。

## Analyze 構文

```python
func.repeat(<str>, <n>)
```

## Analyze の例

```python
func.repeat('ab', 3)

┌──────────┐
│ 'ababab'  │
└──────────┘
```

## SQL 構文

```sql
REPEAT(<str>, <n>)
```

## SQL の例

```sql
SELECT REPEAT('ab', 3);

┌────────┐
│ ababab  │
└────────┘
```
