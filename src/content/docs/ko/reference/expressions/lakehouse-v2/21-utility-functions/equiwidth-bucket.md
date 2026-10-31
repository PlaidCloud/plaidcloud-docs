---
title: EQUIWIDTH_BUCKET (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 EQUIWIDTH_BUCKET 유틸리티 함수를 사용합니다. 등폭 히스토그램에서 값이 속하는 버킷 번호를 반환하며, [min, max] 범위를 같은 폭의 구간으로 나눕니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/equiwidth-bucket.md
---

등폭 히스토그램에서 값이 속하는 버킷 번호를 반환합니다. [min, max] 범위를 같은 폭의 구간으로 나눕니다.

## Analyze 구문

```python
func.equiwidth_bucket(<expr>, <min>, <max>, <num_buckets>)
```

## Analyze 예제

```python
func.equiwidth_bucket(75, 0, 100, 10)

┌───┐
│ 8 │
└───┘
```

## SQL 구문

```sql
EQUIWIDTH_BUCKET(<expr>, <min>, <max>, <num_buckets>)
```

## SQL 예제

```sql
SELECT score, EQUIWIDTH_BUCKET(score, 0, 100, 10) AS bucket
FROM students;

┌───────┬────────┐
│ score │ bucket │
├───────┼────────┤
│    25 │      3 │
│    75 │      8 │
│    95 │     10 │
└───────┴────────┘
```
