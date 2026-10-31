---
title: FROM_BASE64 (Lakehouse v1)
description: FROM_BASE64 — recebe uma string codificada com as regras de base64 e retorna o resultado decodificado como binário.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/from-base64.md
---

Recebe uma string codificada com as regras de base64 e retorna o resultado decodificado como binário.
O resultado é NULL se o argumento for NULL ou não for uma string base64 válida.

## Sintaxe do Analyze

```python
func.from_base64(<expr>)
```

## Exemplos do Analyze

```python
func.from_base64('YWJj')
┌──────────────────────────┐
│ func.from_base64('YWJj') │
├──────────────────────────┤
│ abc                      │
└──────────────────────────┘
```

## Sintaxe SQL

```sql
FROM_BASE64(<expr>)
```

## Argumentos

| Argumentos | Descrição                |
|-----------|--------------------------|
| `<expr>`  | O valor da string.       |

## Tipo de retorno

`BINARY`

## Exemplos de SQL

```sql
SELECT TO_BASE64('abc'), FROM_BASE64(TO_BASE64('abc')) as b, b::String;
┌───────────────────────────────────────┐
│ to_base64('abc') │    b   │ b::string │
│      String      │ Binary │   String  │
├──────────────────┼────────┼───────────┤
│ YWJj             │ 616263 │ abc       │
└───────────────────────────────────────┘
```
