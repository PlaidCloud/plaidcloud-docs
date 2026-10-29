---
title: FIND_IN_SET（Lakehouse v2）
description: FIND_IN_SET — カンマ区切りのリスト内で文字列が見つかった位置を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/find-in-set.md
---

カンマ区切りのリスト内で文字列が見つかった位置を返します。

## Analyze 構文

```python
func.find_in_set(<str>, <strlist>)
```

## Analyze の例

```python
func.find_in_set('b', 'a,b,c')

┌───┐
│ 2  │
└───┘
```

## SQL 構文

```sql
FIND_IN_SET(<str>, <strlist>)
```

## SQL の例

```sql
SELECT FIND_IN_SET('b', 'a,b,c');

┌───┐
│ 2  │
└───┘
```
