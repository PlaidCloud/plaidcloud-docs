---
title: NOW (Lakehouse v1)
description: NOW — 현재 날짜와 시간을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/now.md
---

현재 날짜와 시간을 반환합니다.

## Analyze 구문

```python
func.now()
```

## Analyze 예시

```python
┌─────────────────────────────────────────────────────────┐
│  func.current_timestamp()  │         func.now()         │
├────────────────────────────┼────────────────────────────┤
│ 2024-01-29 04:38:12.584359 │ 2024-01-29 04:38:12.584417 │
└─────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
NOW()
```

## 반환 형식

TIMESTAMP

## 별칭

- [CURRENT_TIMESTAMP](../current-timestamp)

## SQL 예시

이 예시는 현재 날짜와 시간을 반환합니다.

```sql
SELECT CURRENT_TIMESTAMP(), NOW();

┌─────────────────────────────────────────────────────────┐
│     current_timestamp()    │            now()           │
├────────────────────────────┼────────────────────────────┤
│ 2024-01-29 04:38:12.584359 │ 2024-01-29 04:38:12.584417 │
└─────────────────────────────────────────────────────────┘
```
