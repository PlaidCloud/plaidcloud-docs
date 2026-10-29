---
title: TRIM (Lakehouse v2)
description: TRIM — remove os espaços em branco iniciais e finais, ou os carateres especificados, de uma cadeia.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/trim.md
---

Remove os espaços em branco iniciais e finais, ou os carateres especificados, de uma cadeia.

## Sintaxe do Analyze

```python
func.trim(<str>)
```

## Exemplos do Analyze

```python
func.trim('  hello  ')

┌─────────┐
│ 'hello'  │
└─────────┘
```

## Sintaxe SQL

```sql
TRIM(<str>)
```

## Exemplos SQL

```sql
SELECT TRIM('  hello  ');

┌───────┐
│ hello  │
└───────┘
```
