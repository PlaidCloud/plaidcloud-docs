---
title: H3_TO_PARENT (Lakehouse v1)
description: H3_TO_PARENT — 해상도 parent_res에서 h3를 포함하는 부모 인덱스를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-parent.md
---

해상도 `parent_res`에서 `h3`를 포함하는 부모 인덱스를 반환합니다. 0을 반환하면 오류가 발생한 것입니다.

## Analyze 구문

```python
func.h3_to_parent(h3, parent_res)
```

## Analyze 예제

```python
func.h3_to_parent(635318325446452991, 12)

┌───────────────────────────────────────────┐
│ func.h3_to_parent(635318325446452991, 12) │
├───────────────────────────────────────────┤
│                        630814725819082751 │
└───────────────────────────────────────────┘
```

## SQL 구문

```sql
H3_TO_PARENT(h3, parent_res)
```

## SQL 예제

```sql
SELECT H3_TO_PARENT(635318325446452991, 12);

┌──────────────────────────────────────┐
│ h3_to_parent(635318325446452991, 12) │
├──────────────────────────────────────┤
│                   630814725819082751 │
└──────────────────────────────────────┘
```
