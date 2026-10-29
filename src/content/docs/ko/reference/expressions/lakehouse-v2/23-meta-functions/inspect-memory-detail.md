---
title: INSPECT_MEMORY_DETAIL (Lakehouse v2)
description: INSPECT_MEMORY_DETAIL — 메모리 사용량에 대한 상세 정보를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-memory-detail.md
---

메모리 사용량에 대한 상세 정보를 반환합니다.

## Analyze 구문

```python
func.inspect_memory_detail()
```

## Analyze 예제

```python
func.inspect_memory_detail()

┌──────────┐
│ (detail)  │
└──────────┘
```

## SQL 구문

```sql
INSPECT_MEMORY_DETAIL()
```

## SQL 예제

```sql
SELECT * FROM TABLE(INSPECT_MEMORY_DETAIL());

┌─────────────────┐
│ (memory detail)  │
└─────────────────┘
```
