---
title: SUBSTRING_INDEX (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 SUBSTRING_INDEX 문자열 함수를 사용합니다. 구분자가 지정한 횟수만큼 나타나기 전 또는 후의 부분 문자열을 반환합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/substring-index.md
---

구분자가 지정한 횟수만큼 나타나기 전 또는 후의 부분 문자열을 반환합니다.

## Analyze 구문

```python
func.substring_index(<str>, <delim>, <count>)
```

## Analyze 예제

```python
func.substring_index('www.example.com', '.', 2)

┌───────────────┐
│ 'www.example'  │
└───────────────┘
```

## SQL 구문

```sql
SUBSTRING_INDEX(<str>, <delim>, <count>)
```

## SQL 예제

```sql
SELECT SUBSTRING_INDEX('www.example.com', '.', 2);

┌─────────────┐
│ www.example  │
└─────────────┘
```
