---
title: INSPECT_MEMORY (Lakehouse v2)
description: INSPECT_MEMORY — 현재 노드의 메모리 사용량 정보를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/23-meta-functions/inspect-memory.md
---

현재 노드의 메모리 사용량 정보를 반환합니다.

## Analyze 구문

```python
func.inspect_memory()
```

## Analyze 예제

```python
func.inspect_memory()

┌───────────────┐
│ (memory info)  │
└───────────────┘
```

## SQL 구문

```sql
INSPECT_MEMORY()
```

## SQL 예제

```sql
SELECT * FROM TABLE(INSPECT_MEMORY());

┌──────────────────┐
│ (memory details)  │
└──────────────────┘
```
