---
title: ARRAYS_ZIP (Lakehouse v2)
description: ARRAYS_ZIP — 여러 배열을 구조체 배열로 병합합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/02-array-functions/arrays-zip.md
---

여러 배열을 구조체 배열로 병합합니다.

## Analyze 구문

```python
func.arrays_zip([1,2], ['a','b'])
```

## Analyze 예제

```python
func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])

┌───────────────────────────┐
│ [{1,'a'},{2,'b'},{3,'c'}] │
└───────────────────────────┘
```

## SQL 구문

```sql
ARRAYS_ZIP([1,2], ['a','b'])
```

## SQL 예제

```sql
SELECT ARRAYS_ZIP([1, 2, 3], ['a', 'b', 'c']);

┌───────────────────────────────────────────────────┐
│ [{"0":1,"1":"a"},{"0":2,"1":"b"},{"0":3,"1":"c"}] │
└───────────────────────────────────────────────────┘
```
