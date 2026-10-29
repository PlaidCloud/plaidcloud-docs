---
title: VERSION (Lakehouse v1)
description: VERSION — retorna a versão atual do PlaidCloud LakehouseQuery.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/version.md
---

Retorna a versão atual do PlaidCloud LakehouseQuery.

## Sintaxe no Analyze

```sql
func.version()
```

## Exemplos no Analyze

```sql
func.version()

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                           func.version()                                                  │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PlaidCloud LakehouseQuery v1.2.252-nightly-193ed56304(rust-1.75.0-nightly-2023-12-12T22:07:25.371440000Z) │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Sintaxe SQL

```sql
VERSION()
```

## Exemplos de SQL

```sql
SELECT VERSION();

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                version()                                                  │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PlaidCloud LakehouseQuery v1.2.252-nightly-193ed56304(rust-1.75.0-nightly-2023-12-12T22:07:25.371440000Z) │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
