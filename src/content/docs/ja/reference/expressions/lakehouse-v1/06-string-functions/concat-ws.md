---
title: CONCAT_WS (Lakehouse v1)
description: CONCAT_WS — CONCAT_WS() は Concatenate With Separator（区切り文字付き連結）の略で、CONCAT() の特殊な形式です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/concat-ws.md
---

CONCAT_WS() は Concatenate With Separator（区切り文字付き連結）の略で、CONCAT() の特殊な形式です。最初の引数は、残りの引数に対する区切り文字です。区切り文字は、連結する文字列の間に挿入されます。区切り文字も残りの引数も文字列を指定できます。区切り文字が NULL の場合、結果は NULL になります。

CONCAT_WS() は空文字列をスキップしません。ただし、区切り文字の引数の後にある NULL 値はスキップします。

## Analyze の構文

```python
func.concat_ws(<separator>, <expr1>, ...)
```

## Analyze の例

```python
func.concat_ws(',', 'data', 'fuse', 'labs', '2021')
┌─────────────────────────────────────────────────────┐
│ func.concat_ws(',', 'data', 'fuse', 'labs', '2021') │
├─────────────────────────────────────────────────────┤
│ data,fuse,labs,2021                                 │
└─────────────────────────────────────────────────────┘
```

## SQL構文

```sql
CONCAT_WS(<separator>, <expr1>, ...)
```

## 引数

| 引数     | 説明   |
|---------------| ------------- |
| `<separator>` | 文字列列 |
| `<expr1>`     | 値の列  |

## 戻り値の型

`VARCHAR` 型の値または `NULL` 型。

## SQLの例

```sql
SELECT CONCAT_WS(',', 'data', 'fuse', 'labs', '2021');
┌────────────────────────────────────────────────┐
│ CONCAT_WS(',', 'data', 'fuse', 'labs', '2021') │
├────────────────────────────────────────────────┤
│ data,fuse,labs,2021                            │
└────────────────────────────────────────────────┘

SELECT CONCAT_WS(',', 'data', NULL, 'bend');
┌──────────────────────────────────────┐
│ CONCAT_WS(',', 'data', NULL, 'bend') │
├──────────────────────────────────────┤
│ data,bend                            │
└──────────────────────────────────────┘


SELECT CONCAT_WS(',', 'data', NULL, NULL, 'bend');
┌────────────────────────────────────────────┐
│ CONCAT_WS(',', 'data', NULL, NULL, 'bend') │
├────────────────────────────────────────────┤
│ data,bend                                  │
└────────────────────────────────────────────┘


SELECT CONCAT_WS(NULL, 'data', 'fuse', 'labs');
┌─────────────────────────────────────────┐
│ CONCAT_WS(NULL, 'data', 'fuse', 'labs') │
├─────────────────────────────────────────┤
│                                    NULL │
└─────────────────────────────────────────┘

SELECT CONCAT_WS(',', NULL);
┌──────────────────────┐
│ CONCAT_WS(',', NULL) │
├──────────────────────┤
│                      │
└──────────────────────┘
```
