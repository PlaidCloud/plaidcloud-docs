---
title: BAR (Lakehouse v2)
description: "PlaidCloud Lakehouse에서 BAR 유틸리티 함수를 사용합니다. 범위 내 값을 시각적인 막대 문자열로 표현하여 반환하며, 텍스트 기반 시각화에 유용합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/bar.md
---

범위 내 값을 시각적인 막대 문자열로 표현하여 반환합니다. 텍스트 기반 시각화에 유용합니다.

## Analyze 구문

```python
func.bar(<value>, <min>, <max>, <width>)
```

## Analyze 예제

```python
func.bar(50, 0, 100, 20)

┌──────────────────────┐
│ ██████████           │
└──────────────────────┘
```

## SQL 구문

```sql
BAR(<value>, <min>, <max>, <width>)
```

## SQL 예제

```sql
SELECT score, BAR(score, 0, 100, 20) AS bar FROM students;

┌───────┬──────────────────────┐
│ score │ bar                  │
├───────┼──────────────────────┤
│    25 │ █████                │
│    50 │ ██████████           │
│    75 │ ███████████████      │
│   100 │ ████████████████████ │
└───────┴──────────────────────┘
```
