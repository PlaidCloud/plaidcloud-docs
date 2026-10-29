---
title: TRIM (Lakehouse v1)
description: TRIM — 지정한 제거 문자열이 앞이나 뒤에 나타나는 경우를 모두 제거한 문자열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/trim.md
---

지정한 제거 문자열이 앞이나 뒤에 나타나는 경우를 모두 제거한 문자열을 반환합니다. 제거 문자열을 생략하면 공백이 제거됩니다.

Analyze 함수는 앞뒤 공백을 자동으로 모두 제거합니다.

## Analyze 구문

```python
func.trim(str)
```

## Analyze 예제

```python
func.trim('   plaidcloud   ')
┌────────────────────────────────┐
│ func.trim('   plaidcloud   ') │
├────────────────────────────────┤
│ 'plaidcloud'                   │
└────────────────────────────────┘
```

## SQL 구문

```sql
TRIM([{BOTH | LEADING | TRAILING} [remstr] FROM ] str)
```

## SQL 예제

참고로 이 섹션의 모든 예제는 문자열 'databend'를 반환합니다.

다음 예제는 문자열 'xxxdatabendxxx'에서 앞뒤의 문자열 'xxx'를 제거합니다.

```sql
SELECT TRIM(BOTH 'xxx' FROM 'xxxdatabendxxx');
```

다음 예제는 문자열 'xxxdatabend'에서 앞의 문자열 'xxx'를 제거합니다.

```sql
SELECT TRIM(LEADING 'xxx' FROM 'xxxdatabend' );
```
다음 예제는 문자열 'databendxxx'에서 뒤의 문자열 'xxx'를 제거합니다.

```sql
SELECT TRIM(TRAILING 'xxx' FROM 'databendxxx' );
```

제거 문자열을 지정하지 않으면 함수는 앞뒤 공백을 모두 제거합니다. 다음 예제는 앞 공백, 뒤 공백 또는 둘 다를 제거합니다.

```sql
SELECT TRIM('   databend   ');
SELECT TRIM('   databend');
SELECT TRIM('databend   ');
```
