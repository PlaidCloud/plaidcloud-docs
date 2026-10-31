---
title: RAND() (Lakehouse v1)
description: RAND() — 0 <= v < 1 범위의 임의 부동 소수점 값 v를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/rand.md
---

0 &lt;= v &lt; 1.0 범위의 임의 부동 소수점 값 v를 반환합니다. i &lt;= R &lt; j 범위의 임의 정수 R을 얻으려면 FLOOR(i + RAND() * (j − i)) 식을 사용합니다.

## Analyze 구문

```python
func.rand()
```

## Analyze 예시

```python
func.rand()

┌────────────────────┐
│    func.rand()     │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```

## SQL 구문

```sql
RAND()
```

## SQL 예시

```sql
SELECT RAND();

┌────────────────────┐
│       rand()       │
├────────────────────┤
│ 0.5191511074382174 │
└────────────────────┘
```
