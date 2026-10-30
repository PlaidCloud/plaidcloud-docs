---
title: TO_MILLISECONDS (Lakehouse v1)
description: TO_MILLISECONDS — 지정한 밀리초 수를 Interval 형식으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-interval-functions/to-milliseconds.md
---

지정한 밀리초 수를 Interval 형식으로 변환합니다.

- 양의 정수, 0, 음의 정수를 입력으로 받습니다.

## Analyze 구문

```python
func.to_milliseconds(<milliseconds>)
```

## Analyze 예제

```python
func.to_milliseconds(2)
┌──────────────────────────────────────────────────────┐
│ func.to_milliseconds(2)                              │
├──────────────────────────────────────────────────────┤
│  0:00:00.002                                         │
└──────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
TO_MILLISECONDS(<milliseconds>)
```

## 반환 형식

Interval(`hh:mm:ss.sss` 형식).

## SQL 예제

```sql
SELECT TO_MILLISECONDS(2), TO_MILLISECONDS(0), TO_MILLISECONDS((- 2));

┌────────────────────────────────────────────────────────────────┐
│ to_milliseconds(2) │ to_milliseconds(0) │ to_milliseconds(- 2) │
├────────────────────┼────────────────────┼──────────────────────┤
│ 0:00:00.002        │ 00:00:00           │ -0:00:00.002         │
└────────────────────────────────────────────────────────────────┘
```
