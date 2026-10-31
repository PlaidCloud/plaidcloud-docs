---
title: SLEEP（Lakehouse v1）
description: SLEEP — 各データブロックで指定した秒数だけスリープします。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-test-functions/sleep.md
---

各データブロックで `seconds` 秒だけスリープします。

!!! warning 
    スリープが必要なテストの用途にのみ使用してください。


## SQLの構文

```sql
SLEEP(seconds)
```

## 引数

| 引数   | 説明 |
| ----------- | ----------- |
| seconds  | 0以上の任意の数値または浮動小数点数の定数列である必要があります。｜

## 戻り値の型

UInt8

## SQLの例

```sql
SELECT sleep(2);
┌──────────┐
│ sleep(2) │
├──────────┤
│        0 │
└──────────┘
```
