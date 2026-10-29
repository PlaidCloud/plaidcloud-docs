---
title: OCTET_LENGTH（Lakehouse v1）
description: OCTET_LENGTH——OCTET_LENGTH() 是 LENGTH() 的同义词。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/octet-length.md
---

OCTET_LENGTH() 是 LENGTH() 的同义词。

## Analyze 语法

```python
func.octet_length(<str>)
```

## Analyze 示例

```python
func.octet_length('databend')
┌───────────────────────────────┐
│ func.octet_length('databend') │
├───────────────────────────────┤
│                             8 │
└───────────────────────────────┘
```

## SQL 语法

```sql
OCTET_LENGTH(<str>)
```

## SQL 示例

```sql
SELECT OCTET_LENGTH('databend');
┌──────────────────────────┐
│ OCTET_LENGTH('databend') │
├──────────────────────────┤
│                        8 │
└──────────────────────────┘
```
