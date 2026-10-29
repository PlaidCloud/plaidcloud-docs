---
title: H3_NUM_HEXAGONS (Lakehouse v1)
description: H3_NUM_HEXAGONS — 지정한 해상도에서 고유한 H3 인덱스의 개수를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-num-hexagons.md
---

지정한 해상도에서 고유한 [H3](https://eng.uber.com/h3/) 인덱스의 개수를 반환합니다. 

## Analyze 구문

```python
func.h3_num_hexagons(res)
```

## Analyze 예제

```python
func.h3_num_hexagons(10)

┌──────────────────────────┐
│ func.h3_num_hexagons(10) │
├──────────────────────────┤
│              33897029882 │
└──────────────────────────┘
```

## SQL 구문

```sql
H3_NUM_HEXAGONS(res)
```

## SQL 예제

```sql
SELECT H3_NUM_HEXAGONS(10);

┌─────────────────────┐
│ h3_num_hexagons(10) │
├─────────────────────┤
│         33897029882 │
└─────────────────────┘
```
