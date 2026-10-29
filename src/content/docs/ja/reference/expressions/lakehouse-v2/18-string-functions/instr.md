---
title: INSTR（Lakehouse v2）
description: INSTR — 文字列内で部分文字列が最初に現れる位置を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/instr.md
---

文字列内で部分文字列が最初に現れる位置を返します。

## Analyze 構文

```python
func.instr(<str>, <substr>)
```

## Analyze の例

```python
func.instr('hello world', 'world')

┌───┐
│ 7  │
└───┘
```

## SQL 構文

```sql
INSTR(<str>, <substr>)
```

## SQL の例

```sql
SELECT INSTR('hello world', 'world');

┌───┐
│ 7  │
└───┘
```
