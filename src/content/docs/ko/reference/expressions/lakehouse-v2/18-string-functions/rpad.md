---
title: RPAD (Lakehouse v2)
description: RPAD — 문자열의 오른쪽을 채움 문자열로 채워 지정한 길이로 만듭니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/rpad.md
---

문자열의 오른쪽을 채움 문자열로 채워 지정한 길이로 만듭니다.

## Analyze 구문

```python
func.rpad(<str>, <len>, <pad>)
```

## Analyze 예제

```python
func.rpad('hello', 10, '.')

┌──────────────┐
│ 'hello.....'  │
└──────────────┘
```

## SQL 구문

```sql
RPAD(<str>, <len>, <pad>)
```

## SQL 예제

```sql
SELECT RPAD('hello', 10, '.');

┌────────────┐
│ hello.....  │
└────────────┘
```
