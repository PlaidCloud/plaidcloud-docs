---
title: CURRENT_VERSION（Lakehouse v2）
description: CURRENT_VERSION — StarRocks の現在のバージョンを返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-version.md
---

StarRocks の現在のバージョンを返します。

## Analyze 構文

```python
func.current_version()
```

## Analyze の例

```python
func.current_version()

┌─────────┐
│ '4.1.0'  │
└─────────┘
```

## SQL 構文

```sql
CURRENT_VERSION()
```

## SQL の例

```sql
SELECT CURRENT_VERSION();

┌──────────────┐
│ 4.1.0-xxxxxx  │
└──────────────┘
```
