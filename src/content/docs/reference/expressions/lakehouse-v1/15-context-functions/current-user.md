---
title: CURRENT_USER
description: "Learn how to use the CURRENT_USER context function in PlaidCloud Lakehouse. Returns the user name and host name combination for the account that the server..."
---

Returns the user name and host name combination for the account that the server used to authenticate the current client. This account determines your access privileges. The return value is a string in the utf8 character set.

## Analyze Syntax

```python
func.current_user()
```

## Analyze Examples

```python
func.current_user()

┌─────────────────────┐
│ func.current_user() │
├─────────────────────┤
│ 'root'@'%'          │
└─────────────────────┘
```

## SQL Syntax

```sql
CURRENT_USER()
```

## SQL Examples

```sql
SELECT CURRENT_USER();

┌────────────────┐
│ current_user() │
├────────────────┤
│ 'root'@'%'     │
└────────────────┘
```
