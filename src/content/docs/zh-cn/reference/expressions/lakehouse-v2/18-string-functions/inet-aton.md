---
title: INET_ATON (Lakehouse v2)
description: INET_ATON：将 IPv4 地址字符串转换为数值。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/inet-aton.md
---

将 IPv4 地址字符串转换为数值。

## Analyze 语法

```python
func.inet_aton(<ip_str>)
```

## Analyze 示例

```python
func.inet_aton('192.168.1.1')

┌────────────┐
│ 3232235777  │
└────────────┘
```

## SQL 语法

```sql
INET_ATON(<ip_str>)
```

## SQL 示例

```sql
SELECT INET_ATON('192.168.1.1');

┌────────────┐
│ 3232235777  │
└────────────┘
```
