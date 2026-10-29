---
title: CONNECTION_ID (Lakehouse v1)
description: CONNECTION_ID — 현재 연결의 연결 ID를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/connection-id.md
---

현재 연결의 연결 ID를 반환합니다.

## Analyze 구문

```python
func.connection_id()
```

## Analyze 예제

```python
func.connection_id()

┌──────────────────────────────────────┐
│       func.connection_id()           │
├──────────────────────────────────────┤
│ 23cb06ec-583e-4eba-b790-7c8cf72a53f8 │
└──────────────────────────────────────┘
```

## SQL 구문

```sql
CONNECTION_ID()
```

## SQL 예제

```sql
SELECT CONNECTION_ID();

┌──────────────────────────────────────┐
│            connection_id()           │
├──────────────────────────────────────┤
│ 23cb06ec-583e-4eba-b790-7c8cf72a53f8 │
└──────────────────────────────────────┘
```
