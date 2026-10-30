---
title: HUMANIZE_NUMBER (Lakehouse v1)
description: HUMANIZE_NUMBER — retorna um número legível.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/20-other-functions/humanize-number.md
---

Retorna um número legível.

## Sintaxe no Analyze

```python
func.humanize_number(x);
```

## Exemplos no Analyze

```python
func.humanize_number(1000 * 1000)
┌─────────────────────────────────────┐
│ func.humanize_number((1000 * 1000)) │
├─────────────────────────────────────┤
│ 1 million                           │
└─────────────────────────────────────┘
```

## Sintaxe SQL

```sql
HUMANIZE_NUMBER(x);
```

## Argumentos

| Argumentos | Descrição                  |
|-----------|----------------------------|
| x         | O tamanho numérico.        |


## Tipo de retorno

String.

## Exemplos de SQL

```sql
SELECT HUMANIZE_NUMBER(1000 * 1000)
┌─────────────────────────┐
│ HUMANIZE_NUMBER((1000 * 1000)) │
├─────────────────────────┤
│ 1 million               │
└─────────────────────────┘
```
