---
title: VERSION (Lakehouse v2)
description: VERSION — StarRocks의 MySQL 프로토콜 버전을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/version.md
---

StarRocks의 MySQL 프로토콜 버전을 반환합니다.

## Analyze 구문

```python
func.version()
```

## Analyze 예제

```python
func.version()

┌─────────┐
│ '5.1.0'  │
└─────────┘
```

## SQL 구문

```sql
VERSION()
```

## SQL 예제

```sql
SELECT VERSION();

┌───────┐
│ 5.1.0  │
└───────┘
```
