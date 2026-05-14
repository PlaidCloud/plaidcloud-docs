---
title: BIT_LENGTH
description: "Learn how to use the BIT_LENGTH string function in PlaidCloud Lakehouse. Return the length of a string in bits. Includes syntax and examples."
---

Return the length of a string in bits.

## Analyze Syntax

```python
func.bit_length(<expr>)
```

## Analyze Examples

```python
func.bit_length('Word')
┌─────────────────────────┐
│ func.bit_length('Word') │
├─────────────────────────┤
│                      32 │
└─────────────────────────┘
```

## SQL Syntax

```sql
BIT_LENGTH(<expr>)
```

## Arguments

| Arguments | Description |
|-----------| ----------- |
| `<expr>`  | The string. |

## Return Type

`BIGINT`

## SQL Examples

```sql
SELECT BIT_LENGTH('Word');
┌────────────────────────────┐
│ SELECT BIT_LENGTH('Word'); │
├────────────────────────────┤
│ 32                         │
└────────────────────────────┘
```
