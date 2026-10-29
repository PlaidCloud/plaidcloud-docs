---
title: Expressões do Lakehouse v1
description: Expressões do Lakehouse v1 baseadas nas funções SQL do Databend, com referências do SQLAlchemy usando o prefixo func.
sidebar:
  label: Lakehouse v1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v1/index.md
---

O Lakehouse v1 é construído sobre o mecanismo SQL [Databend](https://databend.com/). Para cada função abaixo, este site fornece sintaxe e exemplos no formato do PlaidCloud; para a referência canônica upstream (com todos os casos extremos e variações de argumentos), consulte a **[referência de funções SQL do Databend](https://docs.databend.com/sql/sql-functions/)**.

## Funções escalares

- [Funções de matriz](./00-array-functions) — Executam operações com matrizes
- [Funções de expressão bit a bit](./01-bitmap-functions) — Executam operações e manipulações bit a bit
- [Funções de expressão condicional](./03-conditional-functions) — Implementam lógica condicional e instruções case
- [Funções de contexto](./15-context-functions) — Fornecem informações sobre o contexto de execução SQL atual
- [Funções de conversão](./02-conversion-functions) — Convertem tipos de dados e fazem cast de valores
- [Funções de data e hora](./05-datetime-functions) — Manipulam e formatam datas e horas
- [Funções geoespaciais](./09-geo-functions) — Tratam e manipulam dados geoespaciais
- [Funções de geometria](./09-geometry-functions) — Tratam e manipulam dados de geometria geoespacial
- [Funções de intervalo](./05-interval-functions) — Criam e manipulam intervalos de tempo
- [Funções de mapa](./10-map-functions) — Criam e manipulam estruturas de dados de mapa
- [Funções numéricas](./04-numeric-functions) — Executam cálculos e operações numéricas
- [Funções de pesquisa](./10-search-functions) — Localizam valores usando expressões
- [Funções de dados semiestruturados e estruturados](./10-semi-structured-functions) — Trabalham com JSON e outros formatos de dados estruturados
- [Funções de string](./06-string-functions) — Manipulam strings e executam operações com expressões regulares

## Funções de agregação

- [Funções de agregação](./07-aggregate-functions) — Calculam resumos como soma, média, contagem etc.
- [Funções de janela](./08-window-functions) — Fornecem cálculos agregados sobre um intervalo especificado de linhas

## Funções de IA

- [Funções de IA](./11-ai-functions) — Aproveitam recursos de IA e aprendizado de máquina

## Funções especializadas

- [Funções de hash](./12-hash-functions) — Geram valores de hash para segurança e comparação de dados
- [Funções de endereço IP](./14-ip-address-functions) — Manipulam e analisam dados de endereço IP
- [Funções UUID](./13-uuid-functions) — Geram e manipulam UUIDs

## Funções de sistema e de tabela

- [Funções de sequência](./18-sequence-functions) — Geram valores sequenciais
- [Funções de sistema](./16-system-functions) — Acessam informações de nível de sistema e executam operações de controle
- [Funções de tabela](./17-table-functions) — Retornam resultados em formato tabular

## Outras funções

- [Funções de dicionário](./19-dictionary-functions) — Trabalham com estruturas de dados de dicionário
- [Outras funções diversas](./20-other-functions) — Uma coleção de várias outras funções
- [Funções de teste](./19-test-functions) — Funções usadas para fins de teste
