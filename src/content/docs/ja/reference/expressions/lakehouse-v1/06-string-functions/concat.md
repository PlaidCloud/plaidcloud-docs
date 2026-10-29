---
title: CONCAT (Lakehouse v1)
description: CONCAT — 引数を連結した結果の文字列を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/concat.md
---

引数を連結した結果の文字列を返します。引数は1つ以上指定できます。すべての引数が非バイナリ文字列の場合、結果は非バイナリ文字列になります。引数にバイナリ文字列が含まれる場合、結果はバイナリ文字列になります。数値の引数は、同等の非バイナリ文字列形式に変換されます。

## Analyze の構文

```python
func.concat(<expr1>, ...)
```

## Analyze の例

```python
func.concat('data', 'bend')
┌─────────────────────────────┐
│ func.concat('data', 'bend') │
├─────────────────────────────┤
│ databend                    │
└─────────────────────────────┘
```

## SQL構文

```sql
CONCAT(<expr1>, ...)
```

## 引数

| 引数 | 説明 |
|-----------|-------------|
| `<expr1>` | 文字列      |

## 戻り値の型

`VARCHAR` 型の値または `NULL` 型。

## SQLの例

```sql
SELECT CONCAT('data', 'bend');
┌────────────────────────┐
│ concat('data', 'bend') │
├────────────────────────┤
│ databend               │
└────────────────────────┘

SELECT CONCAT('data', NULL, 'bend');
┌──────────────────────────────┐
│ CONCAT('data', NULL, 'bend') │
├──────────────────────────────┤
│                         NULL │
└──────────────────────────────┘

SELECT CONCAT('14.3');
┌────────────────┐
│ concat('14.3') │
├────────────────┤
│ 14.3           │
└────────────────┘
```
