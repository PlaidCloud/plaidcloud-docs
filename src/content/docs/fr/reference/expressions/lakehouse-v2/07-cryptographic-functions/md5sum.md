---
title: MD5SUM (Lakehouse v2)
description: MD5SUM — renvoie le hachage MD5 de plusieurs chaînes concaténées.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5sum.md
---

Renvoie le hachage MD5 de plusieurs chaînes concaténées.

## Syntaxe Analyze

```python
func.md5sum(<str1>[, <str2>, ...])
```

## Exemples Analyze

```python
func.md5sum('hello', 'world')

┌────────────────────────────────────┐
│ 'fc5e038d38a57032085441e7fe7010b0'  │
└────────────────────────────────────┘
```

## Syntaxe SQL

```sql
MD5SUM(<str1>[, <str2>, ...])
```

## Exemples SQL

```sql
SELECT MD5SUM('hello', 'world');

┌──────────────────────────────────┐
│ fc5e038d38a57032085441e7fe7010b0  │
└──────────────────────────────────┘
```
