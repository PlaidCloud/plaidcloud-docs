---
title: INSPECT_ALL_PIPES (Lakehouse v2)
description: INSPECT_ALL_PIPES — 모든 파이프 객체에 대한 정보를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-all-pipes.md
---

모든 파이프 객체에 대한 정보를 반환합니다.

## Analyze 구문

```python
func.inspect_all_pipes()
```

## Analyze 예제

```python
func.inspect_all_pipes()

┌─────────────┐
│ (pipe info)  │
└─────────────┘
```

## SQL 구문

```sql
INSPECT_ALL_PIPES()
```

## SQL 예제

```sql
SELECT * FROM TABLE(INSPECT_ALL_PIPES());

┌────────────────┐
│ (pipe details)  │
└────────────────┘
```
