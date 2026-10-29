---
title: RAND(n) (Lakehouse v1)
description: RAND(n) — 0 &lt;= v &lt; 1.0 범위의 임의 부동 소수점 값 v를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/04-numeric-functions/randn.md
---

0 &lt;= v &lt; 1.0 범위의 임의 부동 소수점 값 v를 반환합니다. i &lt;= R &lt; j 범위의 임의 정수 R을 얻으려면 FLOOR(i + RAND() * (j − i)) 식을 사용합니다. 인수 `n`은 시드 값으로 사용됩니다. 인수 값이 같으면 RAND(n)은 매번 같은 값을 반환하므로 반복 가능한 열 값 시퀀스를 생성합니다.

## Analyze 구문

```python
func.rand( <n>)
```

## Analyze 예시

```python
func.rand(1)

┌────────────────────┐
│    func.rand(1)    │
├────────────────────┤
│ 0.7133693869548766 │
└────────────────────┘
```

## SQL 구문

```sql
RAND( <n>)
```

## SQL 예시

```sql
SELECT RAND(1);

┌────────────────────┐
│       rand(1)      │
├────────────────────┤
│ 0.7133693869548766 │
└────────────────────┘
```
