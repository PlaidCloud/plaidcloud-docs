---
title: LPAD (Lakehouse v1)
description: LPAD — 文字列 str の左側を文字列 padstr で埋めて、len 文字の長さにした文字列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/lpad.md
---

文字列 str の左側を文字列 padstr で埋めて、len 文字の長さにした文字列を返します。
str が len より長い場合は、戻り値が len 文字に切り詰められます。

## Analyze の構文

```python
func.lpad(<str>, <len>, <padstr>)
```

## Analyze の例

```python
func.lpad('hi',4,'??')
┌────────────────────────┐
│ func.lpad('hi',4,'??') │
├────────────────────────┤
│ ??hi                   │
└────────────────────────┘
```

```python
func.lpad('hi',1,'??')
┌────────────────────────┐
│ func.lpad('hi',1,'??') │
├────────────────────────┤
│ h                      │
└────────────────────────┘
```

## SQL構文

```sql
LPAD(<str>, <len>, <padstr>)
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
SELECT LPAD('hi',4,'??');
┌─────────────────────┐
│ LPAD('hi', 4, '??') │
├─────────────────────┤
│ ??hi                │
└─────────────────────┘

SELECT LPAD('hi',1,'??');
┌─────────────────────┐
│ LPAD('hi', 1, '??') │
├─────────────────────┤
│ h                   │
└─────────────────────┘
```
