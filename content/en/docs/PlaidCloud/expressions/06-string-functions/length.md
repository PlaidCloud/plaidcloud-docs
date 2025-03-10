---
title: LENGTH
---

Returns the length of a given input string or binary value. In the case of strings, the length represents the count of characters, with each UTF-8 character considered as a single character. For binary data, the length corresponds to the number of bytes.

# Analyze Syntax

```python
func.length(<expr>)
```

## Analyze Examples

```python
func.length('Hello')
+----------------------+
| func.length('Hello') |
+----------------------+
|                    5 |
+----------------------+
```

## SQL Syntax

```sql
LENGTH(<expr>)
```

## Aliases

- [CHAR_LENGTH](char-length)
- [CHARACTER_LENGTH](character-length)
- [LENGTH_UTF8](length-utf8)

## Return Type

BIGINT

## SQL Examples

```sql
SELECT LENGTH('Hello'), LENGTH_UTF8('Hello'), CHAR_LENGTH('Hello'), CHARACTER_LENGTH('Hello');

┌───────────────────────────────────────────────────────────────────────────────────────────┐
│ length('hello') │ length_utf8('hello') │ char_length('hello') │ character_length('hello') │
├─────────────────┼──────────────────────┼──────────────────────┼───────────────────────────┤
│               5 │                    5 │                    5 │                         5 │
└───────────────────────────────────────────────────────────────────────────────────────────┘
```