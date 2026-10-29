---
title: INITCAP (Lakehouse v2)
description: INITCAP — 문자열에서 각 단어의 첫 글자를 대문자로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/initcap.md
---

문자열에서 각 단어의 첫 글자를 대문자로 변환합니다.

## Analyze 구문

```python
func.initcap(<str>)
```

## Analyze 예제

```python
func.initcap('hello world')

┌───────────────┐
│ 'Hello World'  │
└───────────────┘
```

## SQL 구문

```sql
INITCAP(<str>)
```

## SQL 예제

```sql
SELECT INITCAP('hello world');

┌─────────────┐
│ Hello World  │
└─────────────┘
```
