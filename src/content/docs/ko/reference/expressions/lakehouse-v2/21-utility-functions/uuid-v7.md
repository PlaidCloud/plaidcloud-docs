---
title: UUID_V7 (Lakehouse v2)
description: UUID_V7 — 시간순으로 정렬되는 UUID v7 문자열을 반환합니다. UUID v7 값은 생성 시간 순으로 정렬할 수 있습니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-v7.md
---

시간순으로 정렬되는 UUID v7 문자열을 반환합니다. UUID v7 값은 생성 시간 순으로 정렬할 수 있습니다.

## Analyze 구문

```python
func.uuid_v7()
```

## Analyze 예제

```python
func.uuid_v7()

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```

## SQL 구문

```sql
UUID_V7()
```

## SQL 예제

```sql
SELECT UUID_V7();

┌──────────────────────────────────────┐
│ 018f6b2e-3d4a-7000-8000-abcdef123456 │
└──────────────────────────────────────┘
```
