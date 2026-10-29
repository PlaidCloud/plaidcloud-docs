---
title: STRCMP（Lakehouse v2）
description: "PlaidCloud Lakehouse で STRCMP 文字列関数を使用します。2つの文字列を辞書順で比較します。等しい場合は 0、str1 < str2 の場合は -1、str1 > str2 の場合は 1 を返します。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strcmp.md
---

2つの文字列を辞書順で比較します。等しい場合は 0、str1 &lt; str2 の場合は -1、str1 > str2 の場合は 1 を返します。

## Analyze 構文

```python
func.strcmp(<str1>, <str2>)
```

## Analyze の例

```python
func.strcmp('abc', 'abd')

┌────┐
│ -1  │
└────┘
```

## SQL 構文

```sql
STRCMP(<str1>, <str2>)
```

## SQL の例

```sql
SELECT STRCMP('abc', 'abd');

┌────┐
│ -1  │
└────┘
```
