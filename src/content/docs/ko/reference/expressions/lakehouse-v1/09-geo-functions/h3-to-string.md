---
title: H3_TO_STRING (Lakehouse v1)
description: H3_TO_STRING — 지정한 H3 인덱스의 표현을 문자열 표현으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/h3-to-string.md
---

지정한 [H3](https://eng.uber.com/h3/) 인덱스의 표현을 문자열 표현으로 변환합니다. 

## Analyze 구문

```python
func.h3_to_string(h3)
```

## Analyze 예제

```python
func.h3_to_string(635318325446452991)

┌───────────────────────────────────────┐
│ func.h3_to_string(635318325446452991) │
├───────────────────────────────────────┤
│ 8d11aa6a38826ff                       │
└───────────────────────────────────────┘
```

## SQL 구문

```sql
H3_TO_STRING(h3)
```

## SQL 예제

```sql
SELECT H3_TO_STRING(635318325446452991);

┌──────────────────────────────────┐
│ h3_to_string(635318325446452991) │
├──────────────────────────────────┤
│ 8d11aa6a38826ff                  │
└──────────────────────────────────┘
```
