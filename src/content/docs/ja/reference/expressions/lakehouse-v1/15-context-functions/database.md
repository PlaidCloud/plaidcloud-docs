---
title: DATABASE（Lakehouse v1）
description: DATABASE — 現在選択されているデータベースの名前を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/15-context-functions/database.md
---

現在選択されているデータベースの名前を返します。データベースが選択されていない場合、この関数は `default` を返します。

## Analyzeの構文

```python
func.database()
```

## Analyzeの例

```python
func.database()

┌─────────────────┐
│ func.database() │
├─────────────────┤
│ default         │
└─────────────────┘
```

## SQLの構文

```sql
DATABASE()
```

## SQLの例

```sql
SELECT DATABASE();

┌────────────┐
│ database() │
├────────────┤
│ default    │
└────────────┘
```
