---
title: NULLIF (Lakehouse v1)
description: NULLIF — 두 식이 같으면 NULL을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/03-conditional-functions/nullif.md
---

두 식이 같으면 NULL을 반환합니다. 그렇지 않으면 expr1을 반환합니다. 두 식은 데이터 형식이 같아야 합니다.

## Analyze 구문

```python
func.nullif(<expr1>, <expr2>)
```

## Analyze 예시

```python
func.nullif(0, null) 

┌──────────────────────┐
│ func.nullif(0, null) │
├──────────────────────┤
│                    0 │
└──────────────────────┘
```

## SQL 구문

```sql
NULLIF(<expr1>, <expr2>)
```

## SQL 예시

```sql
SELECT NULLIF(0, NULL);

┌─────────────────┐
│ nullif(0, null) │
├─────────────────┤
│               0 │
└─────────────────┘
```
