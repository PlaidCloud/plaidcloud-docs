---
title: TO_BASE64 (Lakehouse v1)
description: TO_BASE64 — converte o argumento de cadeia de caracteres para a forma codificada em base 64 e devolve o resultado como cadeia de caracteres.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/to-base64.md
---

Converte o argumento de cadeia de caracteres para a forma codificada em base 64 e devolve o resultado como cadeia de caracteres.
Se o argumento não for uma cadeia de caracteres, é convertido numa cadeia de caracteres antes de a conversão ser efetuada.
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

| Argumentos | Descrição  |
|-----------|-------------|
| `<v>`     | O valor.    |

## Tipo de Retorno

`VARCHAR`

## Exemplos SQL

```sql
SELECT TO_BASE64('abc');
┌──────────────────┐
│ TO_BASE64('abc') │
├──────────────────┤
│ YWJj             │
└──────────────────┘
```
