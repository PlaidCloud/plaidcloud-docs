---
title: SLEEP (Lakehouse v1)
description: SLEEP — espera o número de segundos indicado em cada bloco de dados.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/19-test-functions/sleep.md
---

Espera `seconds` segundos em cada bloco de dados.

!!! warning 
    Utilizar apenas em testes em que seja necessária uma espera.


## Sintaxe SQL

```sql
SLEEP(seconds)
```

## Argumentos

| Argumentos  | Descrição |
| ----------- | ----------- |
| seconds  | Tem de ser uma coluna constante de qualquer número não negativo ou decimal.｜

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
