---
title: SPACE (Lakehouse v2)
description: SPACE — 지정한 개수의 공백으로 이루어진 문자열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/space.md
---

지정한 개수의 공백으로 이루어진 문자열을 반환합니다.

## Analyze 구문

```python
func.space(<n>)
```

## Analyze 예제

```python
func.space(5)

┌─────────┐
│ '     '  │
└─────────┘
```

## SQL 구문

```sql
SPACE(<n>)
```

## SQL 예제

```sql
SELECT CONCAT('>', SPACE(5), '<');

┌─────────┐
│ >     <  │
└─────────┘
```
