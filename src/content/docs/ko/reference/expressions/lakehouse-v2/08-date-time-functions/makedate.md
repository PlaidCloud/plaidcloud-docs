---
title: MAKEDATE (Lakehouse v2)
description: MAKEDATE — 연도와 연중 일 값으로 날짜를 생성합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/08-date-time-functions/makedate.md
---

연도와 연중 일 값으로 날짜를 생성합니다.

## Analyze 구문

```python
func.makedate(<year>, <dayofyear>)
```

## Analyze 예제

```python
func.makedate(2024, 100)

┌──────────────┐
│ '2024-04-09'  │
└──────────────┘
```

## SQL 구문

```sql
MAKEDATE(<year>, <dayofyear>)
```

## SQL 예제

```sql
SELECT MAKEDATE(2024, 100);

┌────────────┐
│ 2024-04-09  │
└────────────┘
```
