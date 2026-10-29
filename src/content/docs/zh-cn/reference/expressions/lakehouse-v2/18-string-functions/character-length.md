---
title: CHARACTER_LENGTH (Lakehouse v2)
description: CHARACTER_LENGTH：返回字符串中的字符数。是 `CHAR_LENGTH` 的别名。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/character-length.md
---

返回字符串中的字符数。是 `CHAR_LENGTH` 的别名。

## Analyze 语法

```python
func.character_length(<str>)
```

## Analyze 示例

```python
func.character_length('hello')

┌───┐
│ 5  │
└───┘
```

## SQL 语法

```sql
CHARACTER_LENGTH(<str>)
```

## SQL 示例

```sql
SELECT CHARACTER_LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
