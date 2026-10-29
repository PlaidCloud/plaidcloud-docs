---
title: UUID_NUMERIC (Lakehouse v2)
description: UUID_NUMERIC — 임의의 UUID를 128비트 LARGEINT 값으로 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-numeric.md
---

임의의 UUID를 128비트 LARGEINT 값으로 반환합니다.

## Analyze 구문

```python
func.uuid_numeric()
```

## Analyze 예제

```python
func.uuid_numeric()

┌────────────┐
│ (largeint)  │
└────────────┘
```

## SQL 구문

```sql
UUID_NUMERIC()
```

## SQL 예제

```sql
SELECT UUID_NUMERIC();

┌─────────────────────────────────────────┐
│ 113304629137197850819971302868472922876  │
└─────────────────────────────────────────┘
```
