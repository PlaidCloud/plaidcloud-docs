---
title: INET_NTOA (Lakehouse v1)
description: INET_NTOA：将 32 位整数转换为 IPv4 地址。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/inet-ntoa.md
---

将 32 位整数转换为 IPv4 地址。

## Analyze 语法

```python
func.inet_ntoa(<int32>)
```

## Analyze 示例

```python
SELECT func.inet_ntoa(16909060)

┌──────────────────────────────┐
│ func.inet_ntoa(16909060)     │
├──────────────────────────────┤
│ 1.2.3.4                      │
└──────────────────────────────┘
```

## SQL 语法

```sql
INET_NOTA( <int32> )
```

## 别名

- [IPV4_NUM_TO_STRING](../ipv4-num-to-string)

## 返回类型

字符串。

## SQL 示例

```sql
SELECT IPV4_NUM_TO_STRING(16909060), INET_NTOA(16909060);

┌────────────────────────────────────────────────────┐
│ ipv4_num_to_string(16909060) │ inet_ntoa(16909060) │
├──────────────────────────────┼─────────────────────┤
│ 1.2.3.4                      │ 1.2.3.4             │
└────────────────────────────────────────────────────┘
```
