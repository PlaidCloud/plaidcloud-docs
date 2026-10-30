---
title: INET_ATON (Lakehouse v1)
description: INET_ATON — IPv4 주소를 32비트 정수로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/inet-aton.md
---

IPv4 주소를 32비트 정수로 변환합니다.

## Analyze 구문

```python
func.inet_aton(<ip>)
```

## Analyze 예제

```python
func.inet_aton('1.2.3.4')

┌───────────────────────────────┐
│ func.inet_aton('1.2.3.4')     │
├───────────────────────────────┤
│                      16909060 │
└───────────────────────────────┘
```

## SQL 구문

```sql
INET_ATON(<ip>)
```

## 별칭

- [IPV4_STRING_TO_NUM](../ipv4-string-to-num)

## 반환 유형

정수.

## SQL 예제

```sql
SELECT IPV4_STRING_TO_NUM('1.2.3.4'), INET_ATON('1.2.3.4');

┌──────────────────────────────────────────────────────┐
│ ipv4_string_to_num('1.2.3.4') │ inet_aton('1.2.3.4') │
├───────────────────────────────┼──────────────────────┤
│                      16909060 │             16909060 │
└──────────────────────────────────────────────────────┘
```
