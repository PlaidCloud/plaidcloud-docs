---
title: VERSION (Lakehouse v1)
description: VERSION — PlaidCloud LakehouseQuery의 현재 버전을 반환합니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/version.md
---

PlaidCloud LakehouseQuery의 현재 버전을 반환합니다.

## Analyze 구문

```sql
func.version()
```

## Analyze 예제

```sql
func.version()

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                           func.version()                                                  │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PlaidCloud LakehouseQuery v1.2.252-nightly-193ed56304(rust-1.75.0-nightly-2023-12-12T22:07:25.371440000Z) │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## SQL 구문

```sql
VERSION()
```

## SQL 예제

```sql
SELECT VERSION();

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                version()                                                  │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PlaidCloud LakehouseQuery v1.2.252-nightly-193ed56304(rust-1.75.0-nightly-2023-12-12T22:07:25.371440000Z) │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
