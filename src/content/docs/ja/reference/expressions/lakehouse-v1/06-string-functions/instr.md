---
title: INSTR (Lakehouse v1)
description: INSTR — 文字列 str の中で部分文字列 substr が最初に現れる位置を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/instr.md
---

文字列 str の中で部分文字列 substr が最初に現れる位置を返します。
引数の順序が逆になる点を除き、LOCATE() の2引数形式と同じです。

## Analyze の構文

```python
func.instr(<str>, <substr>)
```

## Analyze の例

```python
func.instr('foobarbar', 'bar')
┌────────────────────────────────┐
│ func.instr('foobarbar', 'bar') │
├────────────────────────────────┤
│                              4 │
└────────────────────────────────┘
```

## SQL構文

```sql
INSTR(<str>, <substr>)
```

## 引数

| 引数 | 説明    |
|------------|----------------|
| `<str>`    | 文字列。    |
| `<substr>` | 部分文字列。 |

## 戻り値の型

`BIGINT`

## SQLの例

```sql
SELECT INSTR('foobarbar', 'bar');
┌───────────────────────────┐
│ INSTR('foobarbar', 'bar') │
├───────────────────────────┤
│                         4 │
└───────────────────────────┘

SELECT INSTR('xbar', 'foobar');
┌─────────────────────────┐
│ INSTR('xbar', 'foobar') │
├─────────────────────────┤
│                       0 │
└─────────────────────────┘
```
