---
title: RPAD (Lakehouse v1)
description: RPAD — 文字列 str の右側を文字列 padstr で埋めて、len 文字の長さにした文字列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/rpad.md
---

文字列 str の右側を文字列 padstr で埋めて、len 文字の長さにした文字列を返します。
str が len より長い場合は、戻り値が len 文字に切り詰められます。

## Analyze の構文

```python
func.rpad(<str>, <len>, <padstr>)
```

## Analyze の例

```python
func.rpad('hi',5,'?')
┌───────────────────────┐
│ func.rpad('hi',5,'?') │
├───────────────────────┤
│ hi???                 │
└───────────────────────┘

func.rpad('hi',1,'?')
┌───────────────────────┐
│ func.rpad('hi',1,'?') │
├───────────────────────┤
│ h                     │
└───────────────────────┘
```

## SQL構文

```sql
RPAD(<str>, <len>, <padstr>)
```

## 引数

| 引数 | 説明     |
|------------|-----------------|
| `<str>`    | 文字列。     |
| `<len>`    | 長さ。     |
| `<padstr>` | 埋め込みに使う文字列。 |

## 戻り値の型

`VARCHAR`

## SQLの例

```sql
SELECT RPAD('hi',5,'?');
┌────────────────────┐
│ RPAD('hi', 5, '?') │
├────────────────────┤
│ hi???              │
└────────────────────┘

SELECT RPAD('hi',1,'?');
┌────────────────────┐
│ RPAD('hi', 1, '?') │
├────────────────────┤
│ h                  │
└────────────────────┘
```
