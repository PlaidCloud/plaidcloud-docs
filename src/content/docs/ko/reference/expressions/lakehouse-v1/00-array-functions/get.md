---
title: "GET (배열, Lakehouse v1)"
description: GET — 인덱스(1부터 시작)로 배열에서 요소를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/00-array-functions/get.md
---

인덱스(1부터 시작)로 배열에서 요소를 반환합니다.

## Analyze 구문

```python
func.get( <array>, <index> )
```

## Analyze 예제

```python
func.get([1, 2], 2)

┌─────────────────────┐
│ func.get([1, 2], 2) │
├─────────────────────┤
│                   2 │
└─────────────────────┘
```

## SQL 구문

```sql
GET( <array>, <index> )
```

## 별칭

- [ARRAY_GET](../array-get)

## SQL 예제

```sql
SELECT GET([1, 2], 2), ARRAY_GET([1, 2], 2);

┌───────────────────────────────────────┐
│ get([1, 2], 2) │ array_get([1, 2], 2) │
├────────────────┼──────────────────────┤
│              2 │                    2 │
└───────────────────────────────────────┘
```
