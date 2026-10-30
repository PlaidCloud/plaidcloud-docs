---
title: TRY_INET_ATON (Lakehouse v1)
description: TRY_INET_ATON — IPv4 주소(점으로 구분된 4개 숫자 문자열)를 32비트 정수 표현으로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/try-inet-aton.md
---

try_inet_aton 함수는 점으로 구분된 4개 숫자 형태의 IPv4 주소 문자열을 받아, 해당 IP 주소의 숫자 값을 정수로 반환합니다.

## Analyze 구문

```python
func.try_inet_aton(<str>)
```

## Analyze 예제

```python
func.try_inet_aton('10.0.5.9')

┌────────────────────────────────┐
│ func.try_inet_aton('10.0.5.9') │
├────────────────────────────────┤
│                      167773449 │
└────────────────────────────────┘
```

## SQL 구문

```sql
TRY_INET_ATON( <str> )
```

## 별칭

- [TRY_IPV4_STRING_TO_NUM](../try-ipv4-string-to-num)

## 반환 유형

정수.

## SQL 예제

```sql
SELECT TRY_INET_ATON('10.0.5.9'), TRY_IPV4_STRING_TO_NUM('10.0.5.9');

┌────────────────────────────────────────────────────────────────┐
│ try_inet_aton('10.0.5.9') │ try_ipv4_string_to_num('10.0.5.9') │
│           UInt32          │               UInt32               │
├───────────────────────────┼────────────────────────────────────┤
│                 167773449 │                          167773449 │
└────────────────────────────────────────────────────────────────┘
```
