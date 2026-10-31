---
title: VERSION（Lakehouse v2）
description: VERSION — StarRocks の MySQL プロトコルバージョンを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/version.md
---

StarRocks の MySQL プロトコルバージョンを返します。

## Analyze 構文

```python
func.version()
```

## Analyze の例

```python
func.version()

┌─────────┐
│ '5.1.0'  │
└─────────┘
```

## SQL 構文

```sql
VERSION()
```

## SQL の例

```sql
SELECT VERSION();

┌───────┐
│ 5.1.0  │
└───────┘
```
