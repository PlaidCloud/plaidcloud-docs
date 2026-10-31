---
title: TRY_INET_ATON（Lakehouse v1）
description: TRY_INET_ATON — IPv4アドレス（ドット区切りの4つの数値からなる文字列）を32ビット整数表現に変換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/14-ip-address-functions/try-inet-aton.md
---

try_inet_aton関数は、IPv4アドレスのドット区切り表記の文字列を受け取り、指定されたIPアドレスの数値を整数として返します。

## Analyzeの構文

```python
func.try_inet_aton(<str>)
```

## Analyzeの例

```python
func.try_inet_aton('10.0.5.9')

┌────────────────────────────────┐
│ func.try_inet_aton('10.0.5.9') │
├────────────────────────────────┤
│                      167773449 │
└────────────────────────────────┘
```

## SQLの構文

```sql
TRY_INET_ATON( <str> )
```

## エイリアス

- [TRY_IPV4_STRING_TO_NUM](../try-ipv4-string-to-num)

## 戻り値の型

整数。

## SQLの例

```sql
SELECT TRY_INET_ATON('10.0.5.9'), TRY_IPV4_STRING_TO_NUM('10.0.5.9');

┌────────────────────────────────────────────────────────────────┐
│ try_inet_aton('10.0.5.9') │ try_ipv4_string_to_num('10.0.5.9') │
│           UInt32          │               UInt32               │
├───────────────────────────┼────────────────────────────────────┤
│                 167773449 │                          167773449 │
└────────────────────────────────────────────────────────────────┘
```
