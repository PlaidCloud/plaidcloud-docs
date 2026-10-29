---
title: LOG (Lakehouse v2)
description: LOG — 지정한 밑에 대한 숫자의 로그를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/13-math-functions/log.md
---

지정한 밑에 대한 숫자의 로그를 반환합니다.

## Analyze 구문

```python
func.log(<base>, <x>)
```

## Analyze 예제

```python
func.log(10, 100)

┌─────┐
│ 2.0  │
└─────┘
```

## SQL 구문

```sql
LOG(<base>, <x>)
```

## SQL 예제

```sql
SELECT LOG(10, 100);

┌─────┐
│ 2.0  │
└─────┘
```
