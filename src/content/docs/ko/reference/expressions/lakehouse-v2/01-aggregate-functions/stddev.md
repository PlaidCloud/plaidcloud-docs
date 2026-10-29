---
title: STDDEV (Lakehouse v2)
description: STDDEV — 모표준편차를 반환합니다. `STDDEV_POP`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/01-aggregate-functions/stddev.md
---

모표준편차를 반환합니다. `STDDEV_POP`의 별칭입니다.

## Analyze 구문

```python
func.stddev(get_column(table, 'score'))
```

## Analyze 예제

```python
func.stddev(get_column(table, 'score'))

┌───────┐
│ 15.32 │
└───────┘
```

## SQL 구문

```sql
STDDEV(<score>)
```

## SQL 예제

```sql
SELECT STDDEV(score) FROM test_results;

┌───────┐
│ 15.32 │
└───────┘
```
