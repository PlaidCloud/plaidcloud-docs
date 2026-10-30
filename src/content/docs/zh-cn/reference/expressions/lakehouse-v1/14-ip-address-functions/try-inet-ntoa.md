---
title: TRY_INET_NTOA (Lakehouse v1)
description: TRY_INET_NTOA：将网络字节序的 IPv4 地址转换为点分十进制字符串表示，失败时返回 NULL。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/try-inet-ntoa.md
---

接收网络字节序的 IPv4 地址，并以点分十进制字符串形式返回该地址。

## Analyze 语法

```python
func.try_inet_ntoa(<integer>)
```

## Analyze 示例

```python
func.try_inet_ntoaA(167773449)

┌───────────────────────────────┐
│ func.try_inet_ntoa(167773449) │
├───────────────────────────────┤
│ 10.0.5.9                      │
└───────────────────────────────┘
```

## SQL 语法

```sql
TRY_INET_NTOA( <integer> )
```

## 别名

- [TRY_IPV4_NUM_TO_STRING](../try-ipv4-num-to-string)

## 返回类型

字符串。

## SQL 示例

```sql
SELECT TRY_INET_NTOA(167773449), TRY_IPV4_NUM_TO_STRING(167773449);

┌──────────────────────────────────────────────────────────────┐
│ try_inet_ntoa(167773449) │ try_ipv4_num_to_string(167773449) │
├──────────────────────────┼───────────────────────────────────┤
│ 10.0.5.9                 │ 10.0.5.9                          │
└──────────────────────────────────────────────────────────────┘
```
