---
title: REPLACE
---

Returns the string str with all occurrences of the string from_str replaced by the string to_str.

# Analyze Syntax

```python
func.replace(<str>, <from_str>, <to_str>)
```

## Analyze Examples
```python
func.replace(<str>, <from_str>, <to_str>)
+--------------------------------------+
| func.replace('plaidCloud', 'p', 'P') |
+--------------------------------------+
| PlaidCloud                           |
+--------------------------------------+
```

## SQL Syntax

```sql
REPLACE(<str>, <from_str>, <to_str>)
```

## Arguments

| Arguments    | Description      |
|--------------|------------------|
| `<str>`      | The string.      |
| `<from_str>` | The from string. |
| `<to_str>`   | The to string.   |

## Return Type

`VARCHAR`

## SQL Examples

```sql
SELECT REPLACE('www.mysql.com', 'w', 'Ww');
+-------------------------------------+
| REPLACE('www.mysql.com', 'w', 'Ww') |
+-------------------------------------+
| WwWwWw.mysql.com                    |
+-------------------------------------+
```
