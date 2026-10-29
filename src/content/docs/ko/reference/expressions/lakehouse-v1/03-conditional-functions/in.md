---
title: "[ NOT ] IN (Lakehouse v1)"
description: "[ NOT ] IN — 값이 명시적 목록의 항목 중 하나와 같은지(또는 같지 않은지) 확인합니다."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/in.md
---

값이 명시적 목록에 포함되는지(또는 포함되지 않는지) 확인합니다.

## Analyze 구문

```python
table.columns.in_((<value1>, <value2> ...))
```

## Analyze 예시

```python
table.columns.in_((<value1>, <value2> ...))

┌──────────────────────────┐
│ table.column.in_((2, 3)) │
├──────────────────────────┤
│ true                     │
└──────────────────────────┘
```

## SQL 구문

```sql
<value> [ NOT ] IN (<value1>, <value2> ...)
```

## SQL 예시

```sql
SELECT 1 NOT IN (2, 3);

┌────────────────┐
│ 1 not in(2, 3) │
├────────────────┤
│ true           │
└────────────────┘
```
