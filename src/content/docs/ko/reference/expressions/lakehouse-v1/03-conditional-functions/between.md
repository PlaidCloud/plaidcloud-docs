---
title: "[ NOT ] BETWEEN (Lakehouse v1)"
description: "[ NOT ] BETWEEN — 숫자, 문자열 또는 날짜 값이 주어진 범위 안(또는 밖)에 있으면 true입니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/between.md
---

주어진 숫자 또는 문자열 ` <expr>`이 정의된 하한과 상한 사이에 있으면 `true`를 반환합니다.

## Analyze 구문

```python
table.column.between(<lower_limit>, <upper_limit>
```

## Analyze 예제

```python
table.column.between(0, 5)
```

## SQL 구문

```sql
<expr> [ NOT ] BETWEEN <lower_limit> AND <upper_limit>
```

## SQL 예제

```sql
SELECT 'true' WHERE 5 BETWEEN 0 AND 5;

┌────────┐
│ 'true' │
├────────┤
│ true   │
└────────┘

SELECT 'true' WHERE 'data' BETWEEN 'data' AND 'databendcloud';

┌────────┐
│ 'true' │
├────────┤
│ true   │
└────────┘
```
