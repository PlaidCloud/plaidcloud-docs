---
title: VERSION (Lakehouse v1)
description: VERSION：返回 PlaidCloud LakehouseQuery 的当前版本。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/version.md
---

返回 PlaidCloud LakehouseQuery 的当前版本。

## Analyze 语法

```sql
func.version()
```

## Analyze 示例

```sql
func.version()

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                           func.version()                                                  │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PlaidCloud LakehouseQuery v1.2.252-nightly-193ed56304(rust-1.75.0-nightly-2023-12-12T22:07:25.371440000Z) │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 语法

```sql
VERSION()
```

## SQL 示例

```sql
SELECT VERSION();

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                version()                                                  │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PlaidCloud LakehouseQuery v1.2.252-nightly-193ed56304(rust-1.75.0-nightly-2023-12-12T22:07:25.371440000Z) │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
