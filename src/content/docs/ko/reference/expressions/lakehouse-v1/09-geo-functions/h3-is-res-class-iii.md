---
title: H3_IS_RES_CLASS_III (Lakehouse v1)
description: H3_IS_RES_CLASS_III — 지정한 H3 인덱스의 해상도가 Class III 방향인지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-is-res-class-iii.md
---

지정한 [H3](https://eng.uber.com/h3/) 인덱스의 해상도가 Class III 방향인지 확인합니다.

## Analyze 구문

```python
func.h3_is_res_class_iii(h3)
```

## Analyze 예제

```python
func.h3_is_res_class_iii(635318325446452991)

┌──────────────────────────────────────────────┐
│ func.h3_is_res_class_iii(635318325446452991) │
├──────────────────────────────────────────────┤
│ true                                         │
└──────────────────────────────────────────────┘
```

## SQL 구문

```sql
H3_IS_RES_CLASS_III(h3)
```

## SQL 예제

```sql
SELECT H3_IS_RES_CLASS_III(635318325446452991);

┌─────────────────────────────────────────┐
│ h3_is_res_class_iii(635318325446452991) │
├─────────────────────────────────────────┤
│ true                                    │
└─────────────────────────────────────────┘
```
