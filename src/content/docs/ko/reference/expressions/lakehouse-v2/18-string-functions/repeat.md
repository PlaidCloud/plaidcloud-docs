---
title: REPEAT (Lakehouse v2)
description: REPEAT — 문자열을 지정한 횟수만큼 반복합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/repeat.md
---

문자열을 지정한 횟수만큼 반복합니다.

## Analyze 구문

```python
func.repeat(<str>, <n>)
```

## Analyze 예제

```python
func.repeat('ab', 3)

┌──────────┐
│ 'ababab'  │
└──────────┘
```

## SQL 구문

```sql
REPEAT(<str>, <n>)
```

## SQL 예제

```sql
SELECT REPEAT('ab', 3);

┌────────┐
│ ababab  │
└────────┘
```
