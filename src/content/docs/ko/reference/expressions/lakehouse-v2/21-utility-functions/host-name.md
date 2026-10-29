---
title: HOST_NAME (Lakehouse v2)
description: HOST_NAME — 현재 백엔드 노드의 호스트 이름을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/host-name.md
---

현재 백엔드 노드의 호스트 이름을 반환합니다.

## Analyze 구문

```python
func.host_name()
```

## Analyze 예제

```python
func.host_name()

┌─────────────┐
│ 'be-node-1'  │
└─────────────┘
```

## SQL 구문

```sql
HOST_NAME()
```

## SQL 예제

```sql
SELECT HOST_NAME();

┌───────────┐
│ be-node-1  │
└───────────┘
```
