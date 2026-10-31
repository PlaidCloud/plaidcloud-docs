---
title: UUID_NUMERIC（Lakehouse v2）
description: UUID_NUMERIC — ランダムな UUID を128ビットの LARGEINT 値として返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/uuid-numeric.md
---

ランダムな UUID を128ビットの LARGEINT 値として返します。

## Analyze 構文

```python
func.uuid_numeric()
```

## Analyze の例

```python
func.uuid_numeric()

┌────────────┐
│ (largeint)  │
└────────────┘
```

## SQL 構文

```sql
UUID_NUMERIC()
```

## SQL の例

```sql
SELECT UUID_NUMERIC();

┌─────────────────────────────────────────┐
│ 113304629137197850819971302868472922876  │
└─────────────────────────────────────────┘
```
