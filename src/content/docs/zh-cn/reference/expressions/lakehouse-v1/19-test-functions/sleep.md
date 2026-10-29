---
title: SLEEP (Lakehouse v1)
description: SLEEP：在每个数据块上休眠 seconds 秒。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-test-functions/sleep.md
---

在每个数据块上休眠 `seconds` 秒。

!!! warning 
    仅用于需要休眠的测试场景。


## SQL 语法

```sql
SLEEP(seconds)
```

## 参数

| 参数 | 说明 |
| ----------- | ----------- |
| seconds  | 必须是任意非负数或浮点数的常量列。｜

## 返回类型

UInt8

## SQL 示例

```sql
SELECT sleep(2);
┌──────────┐
│ sleep(2) │
├──────────┤
│        0 │
└──────────┘
```
