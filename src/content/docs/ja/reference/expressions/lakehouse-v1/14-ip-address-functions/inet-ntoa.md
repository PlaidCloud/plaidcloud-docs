---
title: INET_NTOA（Lakehouse v1）
description: INET_NTOA — 32ビット整数をIPv4アドレスに変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/inet-ntoa.md
---

32ビット整数をIPv4アドレスに変換します。

## Analyzeの構文

```python
func.inet_ntoa(<int32>)
```

## Analyzeの例

```python
SELECT func.inet_ntoa(16909060)

┌──────────────────────────────┐
│ func.inet_ntoa(16909060)     │
├──────────────────────────────┤
│ 1.2.3.4                      │
└──────────────────────────────┘
```

## SQLの構文

```sql
INET_NOTA( <int32> )
```

## エイリアス

- [IPV4_NUM_TO_STRING](../ipv4-num-to-string)

## 戻り値の型

文字列。

## SQLの例

```sql
SELECT IPV4_NUM_TO_STRING(16909060), INET_NTOA(16909060);

┌────────────────────────────────────────────────────┐
│ ipv4_num_to_string(16909060) │ inet_ntoa(16909060) │
├──────────────────────────────┼─────────────────────┤
│ 1.2.3.4                      │ 1.2.3.4             │
└────────────────────────────────────────────────────┘
```
