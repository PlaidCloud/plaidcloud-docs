---
title: IS_NOT_ERROR (Lakehouse v1)
description: IS_NOT_ERROR — 식이 오류 값인지 나타내는 불리언 값을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/is-not-error.md
---

식이 오류 값인지 나타내는 불리언 값을 반환합니다.

참고: [IS_ERROR](../is-error)

## Analyze 구문

```python
func.is_error( <expr> )
```

## Analyze 예시

```python
# Indicates division by zero, hence an error
func.is_error((1 / 0)), func.is_not_error((1 / 0))

┌─────────────────────────────────────────────────────┐
│ func.is_error((1 / 0)) │ func.is_not_error((1 / 0)) │
├────────────────────────┼────────────────────────────┤
│ true                   │ false                      │
└─────────────────────────────────────────────────────┘

# The conversion to DATE is successful, hence not an error
func.is_error(func.to_date('2024-03-17')), func.is_not_error(func.to_date('2024-03-17'))

┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ func.is_error(func.to_date('2024-03-17')) │ func.is_not_error(func.to_date('2024-03-17')) │
├───────────────────────────────────────────┼───────────────────────────────────────────────┤
│ false                                     │ true                                          │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
IS_NOT_ERROR( <expr> )
```

## 반환 형식

식이 오류가 아니면 `true`를, 그렇지 않으면 `false`를 반환합니다.

## SQL 예시

```sql
-- Indicates division by zero, hence an error
SELECT IS_ERROR(1/0), IS_NOT_ERROR(1/0);

┌───────────────────────────────────────────┐
│ is_error((1 / 0)) │ is_not_error((1 / 0)) │
├───────────────────┼───────────────────────┤
│ true              │ false                 │
└───────────────────────────────────────────┘

-- The conversion to DATE is successful, hence not an error
SELECT IS_ERROR('2024-03-17'::DATE), IS_NOT_ERROR('2024-03-17'::DATE);

┌─────────────────────────────────────────────────────────────────┐
│ is_error('2024-03-17'::date) │ is_not_error('2024-03-17'::date) │
├──────────────────────────────┼──────────────────────────────────┤
│ false                        │ true                             │
└─────────────────────────────────────────────────────────────────┘
```
