---
title: CONCAT (Lakehouse v1)
description: CONCAT — 인수를 연결한 결과 문자열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/concat.md
---

인수를 연결한 결과 문자열을 반환합니다. 인수는 하나 이상일 수 있습니다. 모든 인수가 비이진 문자열이면 결과도 비이진 문자열입니다. 인수에 이진 문자열이 하나라도 포함되어 있으면 결과는 이진 문자열입니다. 숫자 인수는 이에 해당하는 비이진 문자열 형태로 변환됩니다.

## Analyze 구문

```python
func.concat(<expr1>, ...)
```

## Analyze 예제

```python
func.concat('data', 'bend')
┌─────────────────────────────┐
│ func.concat('data', 'bend') │
├─────────────────────────────┤
│ databend                    │
└─────────────────────────────┘
```

## SQL 구문

```sql
CONCAT(<expr1>, ...)
```

## 인수

| 인수 | 설명 |
|-----------|-------------|
| `<expr1>` | 문자열      |

## 반환 형식

`VARCHAR` 데이터 형식 값 또는 `NULL` 데이터 형식입니다.

## SQL 예제

```sql
SELECT CONCAT('data', 'bend');
┌────────────────────────┐
│ concat('data', 'bend') │
├────────────────────────┤
│ databend               │
└────────────────────────┘

SELECT CONCAT('data', NULL, 'bend');
┌──────────────────────────────┐
│ CONCAT('data', NULL, 'bend') │
├──────────────────────────────┤
│                         NULL │
└──────────────────────────────┘

SELECT CONCAT('14.3');
┌────────────────┐
│ concat('14.3') │
├────────────────┤
│ 14.3           │
└────────────────┘
```
