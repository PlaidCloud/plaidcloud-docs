---
title: CHARACTER_LENGTH（Lakehouse v2）
description: CHARACTER_LENGTH — 文字列の文字数を返します。`CHAR_LENGTH` の別名です。
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/character-length.md
---

文字列の文字数を返します。`CHAR_LENGTH` の別名です。

## Analyze 構文

```python
func.character_length(<str>)
```

## Analyze の例

```python
func.character_length('hello')

┌───┐
│ 5  │
└───┘
```

## SQL 構文

```sql
CHARACTER_LENGTH(<str>)
```

## SQL の例

```sql
SELECT CHARACTER_LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
