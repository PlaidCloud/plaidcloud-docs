---
title: ASCII (Lakehouse v2)
description: ASCII — 문자열 첫 번째 문자의 ASCII 코드를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ascii.md
---

문자열 첫 번째 문자의 ASCII 코드를 반환합니다.

## Analyze 구문

```python
func.ascii(<str>)
```

## Analyze 예제

```python
func.ascii('A')

┌────┐
│ 65  │
└────┘
```

## SQL 구문

```sql
ASCII(<str>)
```

## SQL 예제

```sql
SELECT ASCII('A');

┌────┐
│ 65  │
└────┘
```
