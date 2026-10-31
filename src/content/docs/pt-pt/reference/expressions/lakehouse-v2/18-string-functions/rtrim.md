---
title: RTRIM (Lakehouse v2)
description: RTRIM — remove os espaços em branco finais ou os carateres especificados do fim de uma cadeia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/rtrim.md
---

Remove os espaços em branco finais ou os carateres especificados do fim de uma cadeia.

## Sintaxe do Analyze

```python
func.rtrim(<str>)
```

## Exemplos do Analyze

```python
func.rtrim('hello   ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Sintaxe SQL

```sql
RTRIM(<str>)
```

## Exemplos SQL

```sql
SELECT RTRIM('hello   ');

┌───────┐
│ hello  │
└───────┘
```
