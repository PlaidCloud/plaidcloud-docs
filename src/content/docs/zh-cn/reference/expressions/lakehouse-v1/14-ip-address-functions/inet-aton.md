---
title: INET_ATON (Lakehouse v1)
description: INET_ATON：将 IPv4 地址转换为 32 位整数。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/inet-aton.md
---

将 IPv4 地址转换为 32 位整数。

## Analyze 语法

```python
func.inet_aton(<ip>)
```

## Analyze 示例

```python
func.inet_aton('1.2.3.4')

┌───────────────────────────────┐
│ func.inet_aton('1.2.3.4')     │
├───────────────────────────────┤
│                      16909060 │
└───────────────────────────────┘
```

## SQL 语法

```sql
INET_ATON(<ip>)
```

## 别名

- [IPV4_STRING_TO_NUM](../ipv4-string-to-num)

## 返回类型

整数。

## SQL 示例

```sql
SELECT IPV4_STRING_TO_NUM('1.2.3.4'), INET_ATON('1.2.3.4');

┌──────────────────────────────────────────────────────┐
│ ipv4_string_to_num('1.2.3.4') │ inet_aton('1.2.3.4') │
├───────────────────────────────┼──────────────────────┤
│                      16909060 │             16909060 │
└──────────────────────────────────────────────────────┘
```
