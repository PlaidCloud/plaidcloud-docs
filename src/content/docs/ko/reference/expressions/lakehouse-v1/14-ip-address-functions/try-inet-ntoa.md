---
title: TRY_INET_NTOA (Lakehouse v1)
description: TRY_INET_NTOA — 네트워크 바이트 순서의 IPv4 주소를 점으로 구분된 4개 숫자 문자열로 변환하며, 실패하면 NULL을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/try-inet-ntoa.md
---

네트워크 바이트 순서의 IPv4 주소를 받아 점으로 구분된 4개 숫자 문자열 형태의 주소를 반환합니다.

## Analyze 구문

```python
func.try_inet_ntoa(<integer>)
```

## Analyze 예제

```python
func.try_inet_ntoaA(167773449)

┌───────────────────────────────┐
│ func.try_inet_ntoa(167773449) │
├───────────────────────────────┤
│ 10.0.5.9                      │
└───────────────────────────────┘
```

## SQL 구문

```sql
TRY_INET_NTOA( <integer> )
```

## 별칭

- [TRY_IPV4_NUM_TO_STRING](../try-ipv4-num-to-string)

## 반환 유형

문자열.

## SQL 예제

```sql
SELECT TRY_INET_NTOA(167773449), TRY_IPV4_NUM_TO_STRING(167773449);

┌──────────────────────────────────────────────────────────────┐
│ try_inet_ntoa(167773449) │ try_ipv4_num_to_string(167773449) │
├──────────────────────────┼───────────────────────────────────┤
│ 10.0.5.9                 │ 10.0.5.9                          │
└──────────────────────────────────────────────────────────────┘
```
