---
title: INTERSECT_COUNT (Lakehouse v2)
description: "PlaidCloud Lakehouse で INTERSECT_COUNT ビットマップ関数を使用します。ディメンションで絞り込んだ複数のビットマップの積集合に含まれる要素数を返します。"
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/05-bitmap-functions/intersect-count.md
---

ディメンションで絞り込んだ複数のビットマップの積集合に含まれる要素数を返します。

## Analyzeの構文

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'dim'), val1, val2)
```

## Analyzeの例

```python
func.intersect_count(get_column(table, 'bm'), get_column(table, 'tag'), 1, 2)

┌─────┐
│ 150 │
└─────┘
```

## SQLの構文

```sql
INTERSECT_COUNT(<bm>, <dim>, val1, val2)
```

## SQLの例

```sql
SELECT INTERSECT_COUNT(user_bm, tag, 1, 2) FROM segments;

┌─────┐
│ 150 │
└─────┘
```
