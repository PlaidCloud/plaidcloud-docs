---
title: H3_INDEXES_ARE_NEIGHBORS (Lakehouse v1)
description: H3_INDEXES_ARE_NEIGHBORS — 지정한 H3 인덱스가 서로 이웃인지 여부를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-indexes-are-neighbors.md
---

지정한 [H3](https://eng.uber.com/h3/) 인덱스가 서로 이웃인지 여부를 반환합니다.

## Analyze 구문

```python
func.h3_indexes_are_neighbors(h3, a_h3)
```

## Analyze 예제

```python
func.h3_indexes_are_neighbors(644325524701193974, 644325524701193897)

┌───────────────────────────────────────────────────────────────────────┐
│ func.h3_indexes_are_neighbors(644325524701193974, 644325524701193897) │
├───────────────────────────────────────────────────────────────────────┤
│ true                                                                  │
└───────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
H3_INDEXES_ARE_NEIGHBORS(h3, a_h3)
```

## SQL 예제

```sql
SELECT H3_INDEXES_ARE_NEIGHBORS(644325524701193974, 644325524701193897);

┌──────────────────────────────────────────────────────────────────┐
│ h3_indexes_are_neighbors(644325524701193974, 644325524701193897) │
├──────────────────────────────────────────────────────────────────┤
│ true                                                             │
└──────────────────────────────────────────────────────────────────┘
```
