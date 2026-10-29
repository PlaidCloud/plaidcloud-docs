---
title: INET_NTOA (Lakehouse v1)
description: INET_NTOA — 32비트 정수를 IPv4 주소로 변환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/inet-ntoa.md
---

32비트 정수를 IPv4 주소로 변환합니다.

## Analyze 구문

```python
func.inet_ntoa(<int32>)
```

## Analyze 예제

```python
SELECT func.inet_ntoa(16909060)

┌──────────────────────────────┐
│ func.inet_ntoa(16909060)     │
├──────────────────────────────┤
│ 1.2.3.4                      │
└──────────────────────────────┘
```

## SQL 구문

```sql
INET_NOTA( <int32> )
```

## 별칭

- [IPV4_NUM_TO_STRING](../ipv4-num-to-string)

## 반환 유형

문자열.

## SQL 예제

```sql
SELECT IPV4_NUM_TO_STRING(16909060), INET_NTOA(16909060);

┌────────────────────────────────────────────────────┐
│ ipv4_num_to_string(16909060) │ inet_ntoa(16909060) │
├──────────────────────────────┼─────────────────────┤
│ 1.2.3.4                      │ 1.2.3.4             │
└────────────────────────────────────────────────────┘
```
