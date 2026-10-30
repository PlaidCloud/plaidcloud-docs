---
title: Expressões do Lakehouse v2
description: Expressões do Lakehouse v2 baseadas nas funções SQL do StarRocks 4.1, com referências do SQLAlchemy.
sidebar:
  label: Lakehouse v2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/index.md
---

O Lakehouse v2 é construído sobre o [StarRocks](https://www.starrocks.io/) 4.1. Para cada função abaixo, este site traz a sintaxe e os exemplos no formato do PlaidCloud; para a referência oficial do projeto de origem (com todos os casos extremos e variações de argumentos), consulte a **[referência de funções SQL do StarRocks](https://docs.starrocks.io/docs/sql-reference/sql-functions/)**.

## Funções de agregação

- [Funções de agregação](./01-aggregate-functions) — Calcule resumos como soma, média, contagem etc.
- [Funções de percentil](./15-percentile-functions) — Calcule valores de percentil e gerencie estados de percentil

## Funções escalares

- [Funções de array](./02-array-functions) — Execute operações com arrays
- [Funções binárias](./03-binary-functions) — Converta entre os formatos binário e string
- [Funções de bits](./04-bit-functions) — Execute operações bit a bit
- [Funções de bitmap](./05-bitmap-functions) — Execute operações e manipulações com bitmaps
- [Funções condicionais](./06-condition-functions) — Implemente lógica condicional e instruções case
- [Funções criptográficas](./07-cryptographic-functions) — Criptografe, descriptografe e gere hash de dados
- [Funções de data e hora](./08-date-time-functions) — Manipule e formate datas e horas
- [Funções de dicionário](./09-dictionary-functions) — Pesquise valores em tabelas de dicionário
- [Funções de hash](./10-hash-functions) — Gere valores de hash com MurmurHash e xxHash
- [Funções JSON](./11-json-functions) — Crie, consulte e manipule dados JSON
- [Funções de mapa](./12-map-functions) — Crie e manipule estruturas de dados de mapa
- [Funções matemáticas](./13-math-functions) — Execute cálculos e operações numéricas
- [Funções de correspondência de padrões](./14-pattern-matching-functions) — Compare strings com LIKE e expressões regulares
- [Funções escalares (HLL)](./16-scalar-functions) — Funções de estimativa de cardinalidade HyperLogLog
- [Funções espaciais](./17-spatial-functions) — Trate e manipule dados geoespaciais
- [Funções de string](./18-string-functions) — Manipule strings e execute operações de texto
- [Funções de struct](./19-struct-functions) — Crie e trabalhe com tipos de dados struct
- [Funções de variant](./22-variant-functions) — Consulte e inspecione tipos de dados VARIANT

## Funções de tabela

- [Funções de tabela](./20-table-functions) — Retornam resultados em formato tabular

## Funções utilitárias e meta

- [Funções utilitárias](./21-utility-functions) — Acesse informações do sistema e utilitários de sessão
- [Funções meta](./23-meta-functions) — Inspecione visões materializadas, memória e diagnósticos

## Gerenciamento do Lakehouse

- [Gerenciamento do Lakehouse](./lakehouse-management/) — execute consultas, navegue pelo catálogo, gerencie armazéns e monitore a computação
