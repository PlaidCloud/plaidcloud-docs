---
title: H3_GET_FACES (Lakehouse v1)
description: H3_GET_FACES — 지정한 H3 인덱스와 교차하는 모든 정이십면체 면을 찾습니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-get-faces.md
---

지정한 [H3](https://eng.uber.com/h3/) 인덱스와 교차하는 모든 정이십면체 면을 찾습니다. 면은 0~19의 정수로 표현됩니다.

## Analyze 구문

```python
func.h3_get_faces(h3)
```

## Analyze 예제

```python
func.h3_get_faces(599119489002373119)

┌───────────────────────────────────────┐
│ func.h3_get_faces(599119489002373119) │
├───────────────────────────────────────┤
│ [0,1,2,3,4]                           │
└───────────────────────────────────────┘
```

## SQL 구문

```sql
H3_GET_FACES(h3)
```

## SQL 예제

```sql
SELECT H3_GET_FACES(599119489002373119);

┌──────────────────────────────────┐
│ h3_get_faces(599119489002373119) │
├──────────────────────────────────┤
│ [0,1,2,3,4]                      │
└──────────────────────────────────┘
```
