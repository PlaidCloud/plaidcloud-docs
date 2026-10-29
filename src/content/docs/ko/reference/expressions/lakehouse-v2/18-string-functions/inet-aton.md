---
title: INET_ATON (Lakehouse v2)
description: INET_ATON — IPv4 주소 문자열을 숫자 값으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/inet-aton.md
---

IPv4 주소 문자열을 숫자 값으로 변환합니다.

## Analyze 구문

```python
func.inet_aton(<ip_str>)
```

## Analyze 예제

```python
func.inet_aton('192.168.1.1')

┌────────────┐
│ 3232235777  │
└────────────┘
```

## SQL 구문

```sql
INET_ATON(<ip_str>)
```

## SQL 예제

```sql
SELECT INET_ATON('192.168.1.1');

┌────────────┐
│ 3232235777  │
└────────────┘
```
