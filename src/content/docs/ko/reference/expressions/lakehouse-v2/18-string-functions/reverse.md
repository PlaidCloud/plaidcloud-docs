---
title: "REVERSE (String, Lakehouse v2)"
description: REVERSE — 문자열을 뒤집습니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/reverse.md
---

문자열을 뒤집습니다.

## Analyze 구문

```python
func.reverse(<str>)
```

## Analyze 예제

```python
func.reverse('hello')

┌─────────┐
│ 'olleh'  │
└─────────┘
```

## SQL 구문

```sql
REVERSE(<str>)
```

## SQL 예제

```sql
SELECT REVERSE('hello');

┌───────┐
│ olleh  │
└───────┘
```
