---
title: H3_IS_PENTAGON (Lakehouse v1)
description: H3_IS_PENTAGON — 지정한 H3 인덱스가 오각형 셀을 나타내는지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-pentagon.md
---

지정한 [H3](https://eng.uber.com/h3/) 인덱스가 오각형 셀을 나타내는지 확인합니다. 

## Analyze 구문

```python
func.h3_is_pentagon(h3)
```

## Analyze 예제

```python
func.h3_is_pentagon(599119489002373119)

┌─────────────────────────────────────────┐
│ func.h3_is_pentagon(599119489002373119) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```

## SQL 구문

```sql
H3_IS_PENTAGON(h3)
```

## SQL 예제

```sql
SELECT H3_IS_PENTAGON(599119489002373119);

┌────────────────────────────────────┐
│ h3_is_pentagon(599119489002373119) │
├────────────────────────────────────┤
│ true                               │
└────────────────────────────────────┘
```
