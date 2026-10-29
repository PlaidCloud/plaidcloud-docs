---
title: CURRENT_CATALOG (Lakehouse v1)
description: CURRENT_CATALOG — 세션에서 현재 사용 중인 카탈로그의 이름을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/current-catalog.md
---

세션에서 현재 사용 중인 카탈로그의 이름을 반환합니다.

## SQL 구문

```sql
CURRENT_CATALOG()
```

## SQL 예제

```sql
SELECT CURRENT_CATALOG();

┌───────────────────┐
│ current_catalog() │
├───────────────────┤
│ default           │
└───────────────────┘
```
