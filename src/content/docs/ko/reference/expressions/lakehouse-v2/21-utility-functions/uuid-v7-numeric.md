---
title: UUID_V7_NUMERIC (Lakehouse v2)
description: UUID_V7_NUMERIC — 시간순으로 정렬되는 UUID v7을 128비트 LARGEINT 값으로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-v7-numeric.md
---

시간순으로 정렬되는 UUID v7을 128비트 LARGEINT 값으로 반환합니다. UUID v7 값은 생성 시간 순으로 정렬할 수 있습니다.

## Analyze 구문

```python
func.uuid_v7_numeric()
```

## Analyze 예제

```python
func.uuid_v7_numeric()

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```

## SQL 구문

```sql
UUID_V7_NUMERIC()
```

## SQL 예제

```sql
SELECT UUID_V7_NUMERIC();

┌────────────────────────────────────┐
│ 2049638230412545024000012345678901 │
└────────────────────────────────────┘
```
