---
title: STRING_TO_H3 (Lakehouse v1)
description: STRING_TO_H3 — 문자열 표현을 H3(uint64) 표현으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/09-geo-functions/string-to-h3.md
---

문자열 표현을 [H3](https://eng.uber.com/h3/)(uint64) 표현으로 변환합니다.

## Analyze 구문

```python
func.string_to_h3(h3)
```

## Analyze 예제

```python
func.string_to_h3('8d11aa6a38826ff')

┌──────────────────────────────────────┐
│ func.string_to_h3('8d11aa6a38826ff') │
├──────────────────────────────────────┤
│                   635318325446452991 │
└──────────────────────────────────────┘
```

## SQL 구문

```sql
STRING_TO_H3(h3)
```

## SQL 예제

```sql
SELECT STRING_TO_H3('8d11aa6a38826ff');

┌─────────────────────────────────┐
│ string_to_h3('8d11aa6a38826ff') │
├─────────────────────────────────┤
│              635318325446452991 │
└─────────────────────────────────┘
```
