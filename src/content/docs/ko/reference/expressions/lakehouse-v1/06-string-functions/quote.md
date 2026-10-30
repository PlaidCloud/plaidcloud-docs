---
title: QUOTE (Lakehouse v1)
description: QUOTE — 문자열을 따옴표로 묶어 SQL 문에서 올바르게 이스케이프된 데이터 값으로 사용할 수 있는 결과를 만듭니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/quote.md
---

문자열을 따옴표로 묶어 SQL 문에서 올바르게 이스케이프된 데이터 값으로 사용할 수 있는 결과를 만듭니다. 

## Analyze 구문

```python
func.quote(<str>)
```

## Analyze 예제

```python
func.quote('Don\'t')
┌──────────────────────┐
│ func.quote('Don\'t') │
├──────────────────────┤
│  Don\'t!             │
└──────────────────────┘
```

## SQL 구문

```sql
QUOTE(<str>)
```

## SQL 예제

```sql
SELECT QUOTE('Don\'t!');
┌─────────────────┐
│ QUOTE('Don't!') │
├─────────────────┤
│ Don\'t!         │
└─────────────────┘

SELECT QUOTE(NULL);
┌─────────────┐
│ QUOTE(NULL) │
├─────────────┤
│        NULL │
└─────────────┘
```
