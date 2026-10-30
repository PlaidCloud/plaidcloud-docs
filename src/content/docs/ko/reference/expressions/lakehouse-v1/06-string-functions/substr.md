---
title: SUBSTR (Lakehouse v1)
description: SUBSTR — 특정 위치에서 시작하는 지정한 개수의 문자로 이루어진 문자열을 추출합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/substr.md
---

지정한 문자열의 특정 위치에서 시작하는 지정한 개수의 문자로 이루어진 문자열을 추출합니다.

- `len` 인수가 없는 형식은 문자열 `str`의 위치 `pos`부터 시작하는 부분 문자열을 반환합니다.
- `len` 인수가 있는 형식은 문자열 `str`의 위치 `pos`부터 시작하는 `len` 문자 길이의 부분 문자열을 반환합니다.

`pos`에 음수 값을 사용할 수도 있습니다. 이 경우 부분 문자열의 시작 위치는 문자열의 처음이 아니라 끝에서 pos개 문자만큼 떨어진 곳입니다. 이 함수의 모든 형식에서 `pos`에 음수 값을 사용할 수 있습니다. `pos`가 0이면 빈 문자열을 반환합니다. 부분 문자열을 추출할 문자열에서 첫 번째 문자의 위치는 1로 계산합니다.

## Analyze 구문

```python
func.substr(<str>, <pos>, <len>)
```

## Analyze 예제

```python
func.substr('Quadratically', 5, 6)
┌────────────────────────────────────┐
│ func.substr('Quadratically', 5, 6) │
├────────────────────────────────────┤
│ ratica                             │
└────────────────────────────────────┘
```

## SQL 구문

```sql
SUBSTR(<str>, <pos>)

SUBSTR(<str>, <pos>, <len>)
```

## 인수

| 인수 | 설명 |
|-----------|--------------------------------------------------------------------------------------------|
| `<str>`   | 문자를 추출할 원본 문자열                                   |
| `<pos>`   | 부분 문자열이 시작되는 위치(1부터 시작)입니다. 음수이면 끝에서부터 계산합니다. |
| `<len>`   | 추출할 부분 문자열의 최대 길이                                             |

## 별칭

- [SUBSTRING](../substring)
- [MID](../mid)

## 반환 형식

VARCHAR

## SQL 예제

```sql
SELECT
  SUBSTRING('Quadratically', 5),
  SUBSTR('Quadratically', 5),
  MID('Quadratically', 5);

┌─────────────────────────────────────────────────────────────────────────────────────────────────┐
│ substring('quadratically' from 5) │ substring('quadratically' from 5) │ mid('quadratically', 5) │
├───────────────────────────────────┼───────────────────────────────────┼─────────────────────────┤
│ ratically                         │ ratically                         │ ratically               │
└─────────────────────────────────────────────────────────────────────────────────────────────────┘

SELECT
  SUBSTRING('Quadratically', 5, 6),
  SUBSTR('Quadratically', 5, 6),
  MID('Quadratically', 5, 6);

┌────────────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│ substring('quadratically' from 5 for 6) │ substring('quadratically' from 5 for 6) │ mid('quadratically', 5, 6) │
├─────────────────────────────────────────┼─────────────────────────────────────────┼────────────────────────────┤
│ ratica                                  │ ratica                                  │ ratica                     │
└────────────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
