---
title: ARRAYS_ZIP (Lakehouse v1)
description: ARRAYS_ZIP — 여러 배열을 하나의 배열 튜플로 병합합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/arrays-zip.md
---

여러 배열을 하나의 배열 튜플로 병합합니다.

## Analyze 구문

```python
func.arrays_zip( <array1> [, ...] )
```

## Analyze 예제

```python
func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])

┌──────────────────────────────────────────────┐
│ func.arrays_zip([1, 2, 3], ['a', 'b', 'c'])  │
├──────────────────────────────────────────────┤
│  [(1,'a'),(2,'b'),(3,'c')]                   │
└──────────────────────────────────────────────┘
```

## SQL 구문

```sql
ARRAYS_ZIP( <array1> [, ...] )
```

## 인수

| 인수 | 설명 |
|------------|-------------------|
| `<arrayN>` | 입력 ARRAY입니다. |

:::note
- 각 배열의 길이는 같아야 합니다.
:::

## 반환 형식

Array(Tuple).

## SQL 예제

```sql
SELECT ARRAYS_ZIP([1, 2, 3], ['a', 'b', 'c']);
┌────────────────────────────────────────┐
│ arrays_zip([1, 2, 3], ['a', 'b', 'c']) │
├────────────────────────────────────────┤
│ [(1,'a'),(2,'b'),(3,'c')]              │
└────────────────────────────────────────┘
```
