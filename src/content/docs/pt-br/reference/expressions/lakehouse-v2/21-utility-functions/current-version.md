---
title: CURRENT_VERSION (Lakehouse v2)
description: CURRENT_VERSION — retorna a versão atual do StarRocks.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/current-version.md
---

Retorna a versão atual do StarRocks.

## Sintaxe do Analyze

```python
func.current_version()
```

## Exemplos do Analyze

```python
func.current_version()

┌─────────┐
│ '4.1.0'  │
└─────────┘
```

## Sintaxe SQL

```sql
CURRENT_VERSION()
```

## Exemplos de SQL

```sql
SELECT CURRENT_VERSION();

┌──────────────┐
│ 4.1.0-xxxxxx  │
└──────────────┘
```
