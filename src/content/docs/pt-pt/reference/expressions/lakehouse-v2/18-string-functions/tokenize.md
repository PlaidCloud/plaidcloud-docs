---
title: TOKENIZE (Lakehouse v2)
description: "Utilize a função de cadeia TOKENIZE no PlaidCloud Lakehouse. Divide uma cadeia numa matriz de termos com o analisador especificado. Útil para pesquisa de texto integral."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/tokenize.md
---

Divide uma cadeia numa matriz de termos com o analisador especificado. Útil em cenários de pesquisa de texto integral.

## Sintaxe do Analyze

```python
func.tokenize('The quick brown fox', 'english')
```

## Exemplos do Analyze

```python
func.tokenize('The quick brown fox', 'english')

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```

## Sintaxe SQL

```sql
TOKENIZE(<str>[, <analyzer>])
```

## Exemplos SQL

```sql
SELECT TOKENIZE('The quick brown fox', 'english');

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```
