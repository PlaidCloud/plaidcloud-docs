---
title: ARRAY_TO_STRING (Lakehouse v1)
description: ARRAY_TO_STRING — 指定した区切り文字を使用して、配列の要素を1つの文字列に連結します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/array-to-string.md
---

指定した区切り文字を使用して、配列の要素を1つの文字列に連結します。

## Analyzeの構文

```python
func.array_to_string( <array>, '<separator>' )
```

## Analyzeの例

```python
func.array_to_string(['apple', 'banana', 'cherry'], ', ') 

┌────────────────────────────────────────────────────────────┐
│ func.array_to_string(['apple', 'banana', 'cherry'], ', ')  │
├────────────────────────────────────────────────────────────┤
│ Apple, Banana, Cherry                                      │
└────────────────────────────────────────────────────────────┘
```

## SQLの構文

```sql
ARRAY_TO_STRING( <array>, '<separator>' )
```

## SQLの例

```sql
SELECT ARRAY_TO_STRING(['Apple', 'Banana', 'Cherry'], ', ');

┌──────────────────────────────────────────────────────┐
│ array_to_string(['apple', 'banana', 'cherry'], ', ') │
├──────────────────────────────────────────────────────┤
│ Apple, Banana, Cherry                                │
└──────────────────────────────────────────────────────┘
```
