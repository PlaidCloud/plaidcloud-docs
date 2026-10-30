---
title: VERSION（Lakehouse v1）
description: VERSION — PlaidCloud LakehouseQueryの現在のバージョンを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/version.md
---

PlaidCloud LakehouseQueryの現在のバージョンを返します。

## Analyzeの構文

```sql
func.version()
```

## Analyzeの例

```sql
func.version()

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                           func.version()                                                  │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PlaidCloud LakehouseQuery v1.2.252-nightly-193ed56304(rust-1.75.0-nightly-2023-12-12T22:07:25.371440000Z) │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQLの構文

```sql
VERSION()
```

## SQLの例

```sql
SELECT VERSION();

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                version()                                                  │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PlaidCloud LakehouseQuery v1.2.252-nightly-193ed56304(rust-1.75.0-nightly-2023-12-12T22:07:25.371440000Z) │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
