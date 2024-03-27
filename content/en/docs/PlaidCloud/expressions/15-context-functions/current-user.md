---
title: CURRENT_USER
---

Returns the user name and host name combination for the account that the server used to authenticate the current client. This account determines your access privileges. The return value is a string in the utf8 character set.

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