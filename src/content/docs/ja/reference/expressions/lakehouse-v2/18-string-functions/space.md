---
title: SPACE（Lakehouse v2）
description: SPACE — 指定した数の空白文字で構成される文字列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/space.md
---

指定した数の空白文字で構成される文字列を返します。

## Analyze 構文

```python
func.space(<n>)
```

## Analyze の例

```python
func.space(5)

┌─────────┐
│ '     '  │
└─────────┘
```

## SQL 構文

```sql
SPACE(<n>)
```

## SQL の例

```sql
SELECT CONCAT('>', SPACE(5), '<');

┌─────────┐
│ >     <  │
└─────────┘
```
