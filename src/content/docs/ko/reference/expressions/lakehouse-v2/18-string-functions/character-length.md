---
title: CHARACTER_LENGTH (Lakehouse v2)
description: CHARACTER_LENGTH — 문자열의 문자 수를 반환합니다. `CHAR_LENGTH`의 별칭입니다.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/character-length.md
---

문자열의 문자 수를 반환합니다. `CHAR_LENGTH`의 별칭입니다.

## Analyze 구문

```python
func.character_length(<str>)
```

## Analyze 예제

```python
func.character_length('hello')

┌───┐
│ 5  │
└───┘
```

## SQL 구문

```sql
CHARACTER_LENGTH(<str>)
```

## SQL 예제

```sql
SELECT CHARACTER_LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
