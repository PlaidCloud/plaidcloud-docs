---
title: TRY_INET_NTOA（Lakehouse v1）
description: TRY_INET_NTOA — ネットワークバイトオーダーのIPv4アドレスをドット区切りの文字列表現に変換します。失敗した場合はNULLを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/try-inet-ntoa.md
---

ネットワークバイトオーダーのIPv4アドレスを受け取り、ドット区切りの文字列表現で返します。

## Analyzeの構文

```python
func.try_inet_ntoa(<integer>)
```

## Analyzeの例

```python
func.try_inet_ntoaA(167773449)

┌───────────────────────────────┐
│ func.try_inet_ntoa(167773449) │
├───────────────────────────────┤
│ 10.0.5.9                      │
└───────────────────────────────┘
```

## SQLの構文

```sql
TRY_INET_NTOA( <integer> )
```

## エイリアス

- [TRY_IPV4_NUM_TO_STRING](../try-ipv4-num-to-string)

## 戻り値の型

文字列。

## SQLの例

```sql
SELECT TRY_INET_NTOA(167773449), TRY_IPV4_NUM_TO_STRING(167773449);

┌──────────────────────────────────────────────────────────────┐
│ try_inet_ntoa(167773449) │ try_ipv4_num_to_string(167773449) │
├──────────────────────────┼───────────────────────────────────┤
│ 10.0.5.9                 │ 10.0.5.9                          │
└──────────────────────────────────────────────────────────────┘
```
