---
title: CHECK_JSON (Lakehouse v1)
description: CHECK_JSON — Verifica a validade de um documento JSON.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/10-semi-structured-functions/check-json.md
---

Verifica a validade de um documento JSON.
Se a cadeia de entrada for um documento JSON válido ou um `NULL`, o resultado é `NULL`.
Se a entrada não puder ser convertida num valor JSON válido, a cadeia de saída contém a mensagem de erro.

## Sintaxe do Analyze

```python
func.check_json(<expr>)
```

## Exemplos do Analyze

```python
func.check_json('[1,2,3]');
┌────────────────────────────┐
│ func.check_json('[1,2,3]') │
├────────────────────────────┤
│ NULL                       │
└────────────────────────────┘
```

## Sintaxe SQL

```sql
CHECK_JSON( <expr> )
```

## Argumentos

| Argumentos | Descrição                        |
|------------|----------------------------------|
| `<expr>`   | Uma expressão do tipo cadeia     |

## Tipo de retorno

Cadeia

## Exemplos de SQL

```sql
SELECT check_json('[1,2,3]');
┌───────────────────────┐
│ check_json('[1,2,3]') │
├───────────────────────┤
│ NULL                  │
└───────────────────────┘

SELECT check_json('{"key":"val"}');
┌─────────────────────────────┐
│ check_json('{"key":"val"}') │
├─────────────────────────────┤
│ NULL                        │
└─────────────────────────────┘

SELECT check_json('{"key":');
┌──────────────────────────────────────────────┐
│ check_json('{"key":')                        │
├──────────────────────────────────────────────┤
│ EOF while parsing a value at line 1 column 7 │
└──────────────────────────────────────────────┘
```
