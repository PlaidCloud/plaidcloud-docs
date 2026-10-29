---
title: CURRENT_VERSION (Lakehouse v2)
description: CURRENT_VERSION — StarRocks의 현재 버전을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-version.md
---

StarRocks의 현재 버전을 반환합니다.

## Analyze 구문

```python
func.current_version()
```

## Analyze 예제

```python
func.current_version()

┌─────────┐
│ '4.1.0'  │
└─────────┘
```

## SQL 구문

```sql
CURRENT_VERSION()
```

## SQL 예제

```sql
SELECT CURRENT_VERSION();

┌──────────────┐
│ 4.1.0-xxxxxx  │
└──────────────┘
```
