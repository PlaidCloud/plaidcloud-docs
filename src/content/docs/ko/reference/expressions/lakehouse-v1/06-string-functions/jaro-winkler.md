---
title: JARO_WINKLER (Lakehouse v1)
description: JARO_WINKLER — 두 문자열 사이의 Jaro-Winkler 거리를 계산합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/jaro-winkler.md
---

두 문자열 사이의 [Jaro-Winkler 거리](https://en.wikipedia.org/wiki/Jaro%E2%80%93Winkler_distance)를 계산합니다. 문자열 간 유사도를 측정하는 데 흔히 사용되며, 값의 범위는 0.0(완전히 다름)에서 1.0(동일한 문자열)까지입니다. 

## Analyze 구문

```python
func.jaro_winkler(<string1>, <string2>)
```

## Analyze 예제

```python
func.jaro_winkler('databend', 'Databend')
┌───────────────────────────────────────────┐
│ func.jaro_winkler('databend', 'Databend') │
├───────────────────────────────────────────┤
│                        0.9166666666666666 │
└───────────────────────────────────────────┘
```

## SQL 구문

```sql
JARO_WINKLER(<string1>, <string2>)
```

## SQL 예제

JARO_WINKLER 함수는 두 입력 문자열 간의 유사도를 나타내는 FLOAT64 값을 반환합니다. 반환 값은 다음 규칙을 따릅니다.

- 유사도 범위: 결과의 범위는 0.0(완전히 다름)에서 1.0(동일)까지입니다.

    ```sql
    SELECT JARO_WINKLER('databend', 'Databend') AS similarity;

    ┌────────────────────┐
    │     similarity     │
    ├────────────────────┤
    │ 0.9166666666666666 │
    └────────────────────┘

    SELECT JARO_WINKLER('databend', 'database') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │        0.9 │
    └────────────┘
    ```
- NULL 처리: string1 또는 string2가 NULL이면 결과는 NULL입니다.

    ```sql
    SELECT JARO_WINKLER('databend', NULL) AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │ NULL       │
    └────────────┘
    ```
- 빈 문자열:
    - 빈 문자열 두 개를 비교하면 1.0을 반환합니다.

    ```sql
    SELECT JARO_WINKLER('', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          1 │
    └────────────┘
    ```
    - 빈 문자열과 비어 있지 않은 문자열을 비교하면 0.0을 반환합니다.

    ```sql
    SELECT JARO_WINKLER('databend', '') AS similarity;

    ┌────────────┐
    │ similarity │
    ├────────────┤
    │          0 │
    └────────────┘
    ```
