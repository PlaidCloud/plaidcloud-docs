---
title: SLEEP (Lakehouse v2)
description: SLEEP — 지정한 초 동안 실행을 일시 중지합니다. 성공하면 0을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/sleep.md
---

지정한 초 동안 실행을 일시 중지합니다. 성공하면 0을 반환합니다.

## Analyze 구문

```python
func.sleep(<seconds>)
```

## Analyze 예제

```python
func.sleep(1)

┌───┐
│ 0  │
└───┘
```

## SQL 구문

```sql
SLEEP(<seconds>)
```

## SQL 예제

```sql
SELECT SLEEP(1);

┌───┐
│ 0  │
└───┘
```
