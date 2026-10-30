---
title: TRY_TO_BINARY (Lakehouse v1)
description: TRY_TO_BINARY — 식을 이진 값으로 변환하며, 실패하면 오류를 발생시키는 대신 NULL을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/02-conversion-functions/try-to-binary.md
---

입력 식을 이진 값으로 변환하는 [TO_BINARY](../to-binary/)의 개선된 버전으로, 변환에 실패하면 오류를 발생시키는 대신 `NULL`을 반환합니다.

참고: [TO_BINARY](../to-binary/)

## Analyze 구문

```python
func.try_to_binary( <expr> )
```

## Analyze 예제

```python
func.try_to_binary('Databend')

┌───────────────────────────────────────┐
│ func.try_to_binary('Databend')        │
├───────────────────────────────────────┤
│  4461746162656E64                     │
└───────────────────────────────────────┘
```

## SQL 구문

```sql
TRY_TO_BINARY( <expr> )
```

## 예제

이 예제는 JSON 데이터를 이진 값으로 성공적으로 변환합니다.

```sql
SELECT TRY_TO_BINARY(PARSE_JSON('{"key":"value", "number":123}')) AS binary_variant_success;

┌──────────────────────────────────────────────────────────────────────────┐
│                              binary_variant                              │
├──────────────────────────────────────────────────────────────────────────┤
│ 40000002100000031000000610000005200000026B65796E756D62657276616C7565507B │
└──────────────────────────────────────────────────────────────────────────┘
```

이 예제는 입력이 `NULL`이면 함수가 변환에 실패함을 보여 줍니다.

```sql
SELECT TRY_TO_BINARY(PARSE_JSON(NULL)) AS binary_variant_invalid_json;

┌─────────────────────────────┐
│ binary_variant_invalid_json │
├─────────────────────────────┤
│ NULL                        │
└─────────────────────────────┘
```
