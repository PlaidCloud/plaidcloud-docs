---
title: BITNOT (Lakehouse v2)
description: BITNOT — retorna o NOT bit a bit de um valor numérico.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/04-bit-functions/bitnot.md
---

Retorna o NOT bit a bit de um valor numérico.

## Sintaxe do Analyze

```python
func.bitnot(<x>)
```

## Exemplos do Analyze

```python
func.bitnot(0)

┌──────┐
│ '-1'  │
└──────┘
```

## Sintaxe SQL

```sql
BITNOT(<x>)
```

## Exemplos SQL

```sql
SELECT BITNOT(0);

┌────┐
│ -1  │
└────┘
```
