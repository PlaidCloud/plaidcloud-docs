---
title: INET_ATON（Lakehouse v2）
description: INET_ATON — IPv4アドレスの文字列を数値に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/inet-aton.md
---

IPv4アドレスの文字列を数値に変換します。

## Analyze 構文

```python
func.inet_aton(<ip_str>)
```

## Analyze の例

```python
func.inet_aton('192.168.1.1')

┌────────────┐
│ 3232235777  │
└────────────┘
```

## SQL 構文

```sql
INET_ATON(<ip_str>)
```

## SQL の例

```sql
SELECT INET_ATON('192.168.1.1');

┌────────────┐
│ 3232235777  │
└────────────┘
```
