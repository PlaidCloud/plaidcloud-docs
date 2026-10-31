---
title: TO_BASE64 (Lakehouse v1)
description: TO_BASE64 — converte o argumento de string para a forma codificada em base64 e retorna o resultado como uma string de caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/to-base64.md
---

Converte o argumento de string para a forma codificada em base64 e retorna o resultado como uma string de caracteres.
Se o argumento não for uma string, ele é convertido em string antes da conversão.
O resultado é NULL se o argumento for NULL.

## Sintaxe do Analyze

```python
func.to_base64(<v>)
```

## Exemplos do Analyze

```python
func.to_base64('abc')
┌───────────────────────┐
│ func.to_base64('abc') │
├───────────────────────┤
│ YWJj                  │
└───────────────────────┘
```

## Sintaxe SQL

```sql
TO_BASE64(<v>)
```

## Argumentos

| Argumentos | Descrição   |
|-----------|--------------|
| `<v>`     | O valor.     |

## Tipo de retorno

`VARCHAR`

## Exemplos de SQL

```sql
SELECT TO_BASE64('abc');
┌──────────────────┐
│ TO_BASE64('abc') │
├──────────────────┤
│ YWJj             │
└──────────────────┘
```
