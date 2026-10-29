---
title: TRY_INET_ATON (Lakehouse v1)
description: TRY_INET_ATON：将 IPv4 地址（点分十进制字符串）转换为其 32 位整数表示。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/try-inet-aton.md
---

try_inet_aton 函数接收字符串形式的 IPv4 地址点分十进制表示，并以整数形式返回该 IP 地址的数值。

## Analyze 语法

```python
func.try_inet_aton(<str>)
```

## Analyze 示例

```python
func.try_inet_aton('10.0.5.9')

┌────────────────────────────────┐
│ func.try_inet_aton('10.0.5.9') │
├────────────────────────────────┤
│                      167773449 │
└────────────────────────────────┘
```

## SQL 语法

```sql
TRY_INET_ATON( <str> )
```

## 别名

- [TRY_IPV4_STRING_TO_NUM](../try-ipv4-string-to-num)

## 返回类型

整数。

## SQL 示例

```sql
SELECT TRY_INET_ATON('10.0.5.9'), TRY_IPV4_STRING_TO_NUM('10.0.5.9');

┌────────────────────────────────────────────────────────────────┐
│ try_inet_aton('10.0.5.9') │ try_ipv4_string_to_num('10.0.5.9') │
│           UInt32          │               UInt32               │
├───────────────────────────┼────────────────────────────────────┤
│                 167773449 │                          167773449 │
└────────────────────────────────────────────────────────────────┘
```
