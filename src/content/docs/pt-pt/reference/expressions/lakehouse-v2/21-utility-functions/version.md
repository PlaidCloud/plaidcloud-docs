---
title: VERSION (Lakehouse v2)
description: VERSION — devolve a versão do protocolo MySQL do StarRocks.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/21-utility-functions/version.md
---

Devolve a versão do protocolo MySQL do StarRocks.

## Sintaxe do Analyze

```python
func.version()
```

## Exemplos do Analyze

```python
func.version()

┌─────────┐
│ '5.1.0'  │
└─────────┘
```

## Sintaxe SQL

```sql
VERSION()
```

## Exemplos SQL

```sql
SELECT VERSION();

┌───────┐
│ 5.1.0  │
└───────┘
```
