---
title: TOKENIZE (Lakehouse v2)
description: "Use a função de string TOKENIZE no PlaidCloud Lakehouse. Divide uma string em um array de termos usando o analisador especificado. Útil para pesquisa de texto completo."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/18-string-functions/tokenize.md
---

Divide uma string em um array de termos usando o analisador especificado. Útil em cenários de pesquisa de texto completo.

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

## Exemplos de SQL

```sql
SELECT TOKENIZE('The quick brown fox', 'english');

┌─────────────────────────┐
│ ["quick","brown","fox"] │
└─────────────────────────┘
```
