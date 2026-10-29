---
title: IS_ROLE_IN_SESSION (Lakehouse v2)
description: IS_ROLE_IN_SESSION — 지정한 역할이 현재 세션에서 활성 상태인지 확인합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/is-role-in-session.md
---

지정한 역할이 현재 세션에서 활성 상태인지 확인합니다.

## Analyze 구문

```python
func.is_role_in_session(<role_name>)
```

## Analyze 예제

```python
func.is_role_in_session('admin')

┌──────┐
│ True  │
└──────┘
```

## SQL 구문

```sql
IS_ROLE_IN_SESSION(<role_name>)
```

## SQL 예제

```sql
SELECT IS_ROLE_IN_SESSION('admin');

┌───┐
│ 1  │
└───┘
```
