---
title: CURRENT_ROLE (Lakehouse v2)
description: CURRENT_ROLE — 현재 활성 역할을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-role.md
---

현재 활성 역할을 반환합니다.

## Analyze 구문

```python
func.current_role()
```

## Analyze 예제

```python
func.current_role()

┌─────────┐
│ 'admin'  │
└─────────┘
```

## SQL 구문

```sql
CURRENT_ROLE()
```

## SQL 예제

```sql
SELECT CURRENT_ROLE();

┌───────┐
│ admin  │
└───────┘
```
