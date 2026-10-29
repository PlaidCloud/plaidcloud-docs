---
title: H3_TO_CENTER_CHILD (Lakehouse v1)
description: H3_TO_CENTER_CHILD — 지정한 해상도의 중심 자식 인덱스를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-center-child.md
---

지정한 해상도의 중심 자식 인덱스를 반환합니다.

## Analyze 구문

```python
func.h3_to_center_child(h3, res)
```

## Analyze 예제

```python
func.h3_to_center_child(599119489002373119, 15)

┌─────────────────────────────────────────────────┐
│ func.h3_to_center_child(599119489002373119, 15) │
├─────────────────────────────────────────────────┤
│                              644155484202336256 │
└─────────────────────────────────────────────────┘
```

## SQL 구문

```sql
H3_TO_CENTER_CHILD(h3, res)
```

## SQL 예제

```sql
SELECT H3_TO_CENTER_CHILD(599119489002373119, 15);

┌────────────────────────────────────────────┐
│ h3_to_center_child(599119489002373119, 15) │
├────────────────────────────────────────────┤
│                         644155484202336256 │
└────────────────────────────────────────────┘
```
