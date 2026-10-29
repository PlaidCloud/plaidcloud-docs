---
title: INET_ATON（Lakehouse v1）
description: INET_ATON — IPv4アドレスを32ビット整数に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/inet-aton.md
---

IPv4アドレスを32ビット整数に変換します。

## Analyzeの構文

```python
func.inet_aton(<ip>)
```

## Analyzeの例

```python
func.inet_aton('1.2.3.4')

┌───────────────────────────────┐
│ func.inet_aton('1.2.3.4')     │
├───────────────────────────────┤
│                      16909060 │
└───────────────────────────────┘
```

## SQLの構文

```sql
INET_ATON(<ip>)
```

## エイリアス

- [IPV4_STRING_TO_NUM](../ipv4-string-to-num)

## 戻り値の型

整数。

## SQLの例

```sql
SELECT IPV4_STRING_TO_NUM('1.2.3.4'), INET_ATON('1.2.3.4');

┌──────────────────────────────────────────────────────┐
│ ipv4_string_to_num('1.2.3.4') │ inet_aton('1.2.3.4') │
├───────────────────────────────┼──────────────────────┤
│                      16909060 │             16909060 │
└──────────────────────────────────────────────────────┘
```
