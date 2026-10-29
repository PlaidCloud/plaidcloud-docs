---
title: CHAR (Lakehouse v1)
description: CHAR — devolve o caráter correspondente a cada número inteiro indicado.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/06-string-functions/char.md
---

Devolve o caráter correspondente a cada número inteiro indicado.

## Sintaxe do Analyze

```python
func.char(N,...)
```

## Exemplos do Analyze

```python
func.char(77,121,83,81,76)
┌─────────────────────────────┐
│ func.char(77,121,83,81,76) │
├─────────────────────────────┤
│ 4D7953514C                  │
└─────────────────────────────┘
```

## Sintaxe SQL

```sql
CHAR(N, ...)
```

## Argumentos

| Argumentos | Descrição        |
|-----------|------------------|
| N         | Coluna numérica  |

## Tipo de Retorno

`BINARY`

## Exemplos SQL

Este exemplo mostra o valor binário devolvido, bem como a respetiva representação em cadeia de caracteres.

```sql
SELECT CHAR(77,121,83,81,76) as a, a::String;
┌────────────────────────┐
│      a     │ a::string │
│   Binary   │   String  │
├────────────┼───────────┤
│ 4D7953514C │ MySQL     │
└────────────────────────┘
```
