---
title: VERSION (Lakehouse v1)
description: VERSION — renvoie la version actuelle de PlaidCloud LakehouseQuery.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/version.md
---

Renvoie la version actuelle de PlaidCloud LakehouseQuery.

## Syntaxe Analyze

```sql
func.version()
```

## Exemples Analyze

```sql
func.version()

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                           func.version()                                                  │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PlaidCloud LakehouseQuery v1.2.252-nightly-193ed56304(rust-1.75.0-nightly-2023-12-12T22:07:25.371440000Z) │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```

## Syntaxe SQL

```sql
VERSION()
```

## Exemples SQL

```sql
SELECT VERSION();

┌───────────────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                                version()                                                  │
├───────────────────────────────────────────────────────────────────────────────────────────────────────────┤
│ PlaidCloud LakehouseQuery v1.2.252-nightly-193ed56304(rust-1.75.0-nightly-2023-12-12T22:07:25.371440000Z) │
└───────────────────────────────────────────────────────────────────────────────────────────────────────────┘
```
