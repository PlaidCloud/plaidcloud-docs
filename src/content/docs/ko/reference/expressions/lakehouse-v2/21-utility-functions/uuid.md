---
title: UUID (Lakehouse v2)
description: UUID — 임의의 UUID 문자열을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid.md
---

임의의 UUID 문자열을 반환합니다.

## Analyze 구문

```python
func.uuid()
```

## Analyze 예제

```python
func.uuid()

┌────────────────────────────────────────┐
│ '550e8400-e29b-41d4-a716-446655440000'  │
└────────────────────────────────────────┘
```

## SQL 구문

```sql
UUID()
```

## SQL 예제

```sql
SELECT UUID();

┌──────────────────────────────────────┐
│ 550e8400-e29b-41d4-a716-446655440000  │
└──────────────────────────────────────┘
```
