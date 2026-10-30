---
title: TIMEZONE (Lakehouse v1)
description: TIMEZONE — 현재 연결의 시간대를 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/05-datetime-functions/timezone.md
---

현재 연결의 시간대를 반환합니다. 

PlaidCloud Lakehouse는 기본 시간대로 UTC(협정 세계시)를 사용하며, 시간대를 현재 지리적 위치에 맞게 변경할 수 있습니다. `timezone` 설정에 지정할 수 있는 값은 https://docs.rs/chrono-tz/latest/chrono_tz/enum.Tz.html 을 참조하십시오. 자세한 내용은 아래 예시를 참조하십시오.

## Analyze 구문

```python
func.timezone()
```

## Analyze 예시

```python
func.timezone()
┌─────────────────────┐
│ timezone            │
├─────────────────────┤
│ UTC                 │
└─────────────────────┘
```

## SQL 구문

```sql
SELECT TIMEZONE();
```

## SQL 예시

```sql
-- Return the current timezone
SELECT TIMEZONE();
┌─────────────────┐
│ TIMEZONE('UTC') │
├─────────────────┤
│ UTC             │
└─────────────────┘

-- Set the timezone to China Standard Time
SET timezone='Asia/Shanghai';

SELECT TIMEZONE();
┌───────────────────────────┐
│ TIMEZONE('Asia/Shanghai') │
├───────────────────────────┤
│ Asia/Shanghai             │
└───────────────────────────┘
```
