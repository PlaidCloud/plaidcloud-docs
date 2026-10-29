---
title: MD5SUM (Lakehouse v2)
description: MD5SUM — devolve o hash MD5 de várias cadeias concatenadas.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/07-cryptographic-functions/md5sum.md
---

Devolve o hash MD5 de várias cadeias concatenadas.

## Sintaxe do Analyze

```python
func.md5sum(<str1>[, <str2>, ...])
```

## Exemplos do Analyze

```python
func.md5sum('hello', 'world')

┌────────────────────────────────────┐
│ 'fc5e038d38a57032085441e7fe7010b0'  │
└────────────────────────────────────┘
```

## Sintaxe SQL

```sql
MD5SUM(<str1>[, <str2>, ...])
```

## Exemplos SQL

```sql
SELECT MD5SUM('hello', 'world');

┌──────────────────────────────────┐
│ fc5e038d38a57032085441e7fe7010b0  │
└──────────────────────────────────┘
```
