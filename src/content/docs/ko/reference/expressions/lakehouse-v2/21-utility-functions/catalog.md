---
title: CATALOG (Lakehouse v2)
description: CATALOG — 현재 카탈로그의 이름을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/catalog.md
---

현재 카탈로그의 이름을 반환합니다.

## Analyze 구문

```python
func.catalog()
```

## Analyze 예제

```python
func.catalog()

┌───────────────────┐
│ 'default_catalog'  │
└───────────────────┘
```

## SQL 구문

```sql
CATALOG()
```

## SQL 예제

```sql
SELECT CATALOG();

┌─────────────────┐
│ default_catalog  │
└─────────────────┘
```
