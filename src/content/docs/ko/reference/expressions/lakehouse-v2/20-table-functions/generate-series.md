---
title: GENERATE_SERIES (Lakehouse v2)
description: GENERATE_SERIES — 시작 값부터 종료 값까지 지정한 간격으로 일련의 값을 생성합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/20-table-functions/generate-series.md
---

시작 값부터 종료 값까지 지정한 간격으로 일련의 값을 생성합니다.

## Analyze 구문

```python
func.generate_series(<start>, <stop>[, <step>])
```

## Analyze 예제

```python
func.generate_series(1, 5)

┌─────────────────┐
│ [1, 2, 3, 4, 5]  │
└─────────────────┘
```

## SQL 구문

```sql
GENERATE_SERIES(<start>, <stop>[, <step>])
```

## SQL 예제

```sql
SELECT * FROM TABLE(GENERATE_SERIES(1, 5));

┌───────────┐
│ 1
2
3
4
5  │
└───────────┘
```
