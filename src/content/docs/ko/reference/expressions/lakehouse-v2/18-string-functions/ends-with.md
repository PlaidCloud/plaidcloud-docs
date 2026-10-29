---
title: ENDS_WITH (Lakehouse v2)
description: ENDS_WITH — 문자열이 지정한 접미사로 끝나는지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/ends-with.md
---

문자열이 지정한 접미사로 끝나는지 확인합니다.

## Analyze 구문

```python
func.ends_with(<str>, <suffix>)
```

## Analyze 예제

```python
func.ends_with('hello world', 'world')

┌───┐
│ 1  │
└───┘
```

## SQL 구문

```sql
ENDS_WITH(<str>, <suffix>)
```

## SQL 예제

```sql
SELECT ENDS_WITH('hello world', 'world');

┌───┐
│ 1  │
└───┘
```
