---
title: SPACE (Lakehouse v1)
description: SPACE — N 個の空白文字で構成される文字列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/space.md
---

N 個の空白文字で構成される文字列を返します。

## Analyze の構文

```python
func.space(<n>)
```

## Analyze の例

```python
func.space(20)
┌─────────────────┐
│ func.space(20)  │
├─────────────────┤
│                 │
└─────────────────┘
```

## SQL構文

```sql
SPACE(<n>);
```

## 引数

| 引数 | 説明          |
|-----------|----------------------|
| `<n>`     | 空白の数 |

## 戻り値の型

文字列データ型の値。

## SQLの例

```sql
SELECT SPACE(20)
┌──────────────────────┐
│ SPACE(20)            │
├──────────────────────┤
│                      │
└──────────────────────┘
```
