---
title: TRANSLATE（Lakehouse v2）
description: TRANSLATE — 文字の対応表に基づいて、文字列内の文字を置換します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/translate.md
---

文字の対応表に基づいて、文字列内の文字を置換します。

## Analyze 構文

```python
func.translate(<str>, <from>, <to>)
```

## Analyze の例

```python
func.translate('hello', 'el', 'ip')

┌─────────┐
│ 'hippo'  │
└─────────┘
```

## SQL 構文

```sql
TRANSLATE(<str>, <from>, <to>)
```

## SQL の例

```sql
SELECT TRANSLATE('hello', 'el', 'ip');

┌───────┐
│ hippo  │
└───────┘
```
