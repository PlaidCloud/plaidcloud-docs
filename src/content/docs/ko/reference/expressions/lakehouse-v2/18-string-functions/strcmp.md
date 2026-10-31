---
title: STRCMP (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 STRCMP 문자열 함수를 사용합니다. 두 문자열을 사전순으로 비교하며, 같으면 0, str1 < str2이면 -1, str1 > str2이면 1을 반환합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/strcmp.md
---

두 문자열을 사전순으로 비교합니다. 같으면 0, str1 &lt; str2이면 -1, str1 > str2이면 1을 반환합니다.

## Analyze 구문

```python
func.strcmp(<str1>, <str2>)
```

## Analyze 예제

```python
func.strcmp('abc', 'abd')

┌────┐
│ -1  │
└────┘
```

## SQL 구문

```sql
STRCMP(<str1>, <str2>)
```

## SQL 예제

```sql
SELECT STRCMP('abc', 'abd');

┌────┐
│ -1  │
└────┘
```
