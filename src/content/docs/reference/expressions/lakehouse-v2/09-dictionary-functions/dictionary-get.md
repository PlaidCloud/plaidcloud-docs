---
title: DICTIONARY_GET (Lakehouse v2)
description: DICTIONARY_GET — returns the value for a specified key from a dictionary object.
---

Returns the value for a specified key from a dictionary object.

## Analyze Syntax

```python
func.dictionary_get(<dict_name>, <key_column>, <key_value>)
```

## Analyze Examples

```python
func.dictionary_get('status_dict', get_column(table, 'status_code'))

┌──────────┐
│ 'Active'  │
└──────────┘
```

## SQL Syntax

```sql
DICTIONARY_GET(<dict_name>, <key_column>, <key_value>)
```

## SQL Examples

```sql
SELECT DICTIONARY_GET('status_dict', status_code) FROM records;

┌────────┐
│ Active  │
└────────┘
```
