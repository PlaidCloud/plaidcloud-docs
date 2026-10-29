---
title: ARRAYS_ZIP (Lakehouse v2)
description: ARRAYS_ZIP — 複数の配列を、構造体の配列にマージします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/arrays-zip.md
---

複数の配列を、構造体の配列にマージします。

## Analyzeの構文

```python
func.arrays_zip([1,2], ['a','b'])
```

## Analyzeの例

```python
func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])

┌───────────────────────────┐
│ [{1,'a'},{2,'b'},{3,'c'}] │
└───────────────────────────┘
```

## SQLの構文

```sql
ARRAYS_ZIP([1,2], ['a','b'])
```

## SQLの例

```sql
SELECT ARRAYS_ZIP([1, 2, 3], ['a', 'b', 'c']);

┌───────────────────────────────────────────────────┐
│ [{"0":1,"1":"a"},{"0":2,"1":"b"},{"0":3,"1":"c"}] │
└───────────────────────────────────────────────────┘
```
