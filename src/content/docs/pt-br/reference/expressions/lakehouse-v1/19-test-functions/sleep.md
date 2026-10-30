---
title: SLEEP (Lakehouse v1)
description: SLEEP — aguarda seconds segundos em cada bloco de dados.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-test-functions/sleep.md
---

Aguarda `seconds` segundos em cada bloco de dados.

!!! warning 
    Usada apenas em testes em que é necessário aguardar.


## Sintaxe SQL

```sql
SLEEP(seconds)
```

## Argumentos

| Argumentos  | Descrição   |
| ----------- | ----------- |
| seconds  | Deve ser uma coluna constante de qualquer número não negativo ou de ponto flutuante.｜

## Tipo de retorno

UInt8

## Exemplos de SQL

```sql
SELECT sleep(2);
┌──────────┐
│ sleep(2) │
├──────────┤
│        0 │
└──────────┘
```
