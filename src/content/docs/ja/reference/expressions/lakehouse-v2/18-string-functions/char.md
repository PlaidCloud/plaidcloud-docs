---
title: CHAR（Lakehouse v2）
description: CHAR — 指定したASCIIコードに対応する文字を返します。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/char.md
---

指定したASCIIコードに対応する文字を返します。

## Analyze 構文

```python
func.char(<code>)
```

## Analyze の例

```python
func.char(65)

┌─────┐
│ 'A'  │
└─────┘
```

## SQL 構文

```sql
CHAR(<code>)
```

## SQL の例

```sql
SELECT CHAR(65);

┌───┐
│ A  │
└───┘
```
