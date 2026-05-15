---
title: CHARACTER_LENGTH (Lakehouse v2)
description: CHARACTER_LENGTH — returns the number of characters in a string. Alias for `CHAR_LENGTH`.
---

Returns the number of characters in a string. Alias for `CHAR_LENGTH`.

## Analyze Syntax

```python
func.character_length(<str>)
```

## Analyze Examples

```python
func.character_length('hello')

┌───┐
│ 5  │
└───┘
```

## SQL Syntax

```sql
CHARACTER_LENGTH(<str>)
```

## SQL Examples

```sql
SELECT CHARACTER_LENGTH('hello');

┌───┐
│ 5  │
└───┘
```
