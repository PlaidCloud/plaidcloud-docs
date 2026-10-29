---
title: TOKENIZE (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 TOKENIZE 문자열 함수를 사용합니다. 지정한 분석기로 문자열을 용어 배열로 토큰화하며, 전체 텍스트 검색에 유용합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/tokenize.md
---

지정한 분석기로 문자열을 용어 배열로 토큰화합니다. 전체 텍스트 검색 시나리오에 유용합니다.

## Analyze 구문

```python
func.tokenize('The quick brown fox', 'english')
```

## Analyze 예제

```python
func.tokenize('The quick brown fox', 'english')

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```

## SQL 구문

```sql
TOKENIZE(<str>[, <analyzer>])
```

## SQL 예제

```sql
SELECT TOKENIZE('The quick brown fox', 'english');

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```
