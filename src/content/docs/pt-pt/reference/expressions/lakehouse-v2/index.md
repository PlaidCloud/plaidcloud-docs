---
title: Expressões do Lakehouse v2
description: Expressões do Lakehouse v2 baseadas nas funções SQL do StarRocks 4.1, com referências SQLAlchemy.
sidebar:
  label: Lakehouse v2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/expressions/lakehouse-v2/index.md
---

O Lakehouse v2 baseia-se no [StarRocks](https://www.starrocks.io/) 4.1. Para cada função abaixo, este site fornece sintaxe e exemplos adaptados ao PlaidCloud; para a referência canónica original (com todos os casos limite e variantes de argumentos), consulte a **[referência de funções SQL do StarRocks](https://docs.starrocks.io/docs/sql-reference/sql-functions/)**.

## Funções de agregação

- [Funções de agregação](./01-aggregate-functions) — Calcule resumos como soma, média, contagem, etc.
- [Funções de percentil](./15-percentile-functions) — Calcule valores de percentil e faça a gestão de estados de percentil

## Funções escalares

- [Funções de matriz](./02-array-functions) — Execute operações com matrizes
- [Funções binárias](./03-binary-functions) — Converta entre formatos binário e de cadeia
- [Funções de bits](./04-bit-functions) — Execute operações bit a bit
- [Funções de bitmap](./05-bitmap-functions) — Execute operações e manipulações com bitmaps
- [Funções de condição](./06-condition-functions) — Implemente lógica condicional e instruções case
- [Funções criptográficas](./07-cryptographic-functions) — Cifre, decifre e gere hashes de dados
- [Funções de data e hora](./08-date-time-functions) — Manipule e formate datas e horas
- [Funções de dicionário](./09-dictionary-functions) — Pesquise valores em tabelas de dicionário
- [Funções de hash](./10-hash-functions) — Gere valores de hash com MurmurHash e xxHash
- [Funções JSON](./11-json-functions) — Crie, consulte e manipule dados JSON
- [Funções de mapa](./12-map-functions) — Crie e manipule estruturas de dados de mapa
- [Funções matemáticas](./13-math-functions) — Execute cálculos e operações numéricas
- [Funções de correspondência de padrões](./14-pattern-matching-functions) — Faça corresponder cadeias com LIKE e expressões regulares
- [Funções escalares (HLL)](./16-scalar-functions) — Funções de estimativa de cardinalidade HyperLogLog
- [Funções espaciais](./17-spatial-functions) — Trate e manipule dados geoespaciais
- [Funções de cadeia](./18-string-functions) — Manipule cadeias e execute operações de texto
- [Funções de struct](./19-struct-functions) — Crie e trabalhe com tipos de dados struct
- [Funções de variant](./22-variant-functions) — Consulte e inspecione tipos de dados VARIANT

## Funções de tabela

- [Funções de tabela](./20-table-functions) — Devolvem resultados em formato tabular

## Funções utilitárias e de metadados

- [Funções utilitárias](./21-utility-functions) — Aceda a informação do sistema e a utilitários de sessão
- [Funções de metadados](./23-meta-functions) — Inspecione vistas materializadas, memória e diagnósticos

## Gerir o Lakehouse

- [Gestão do Lakehouse](./lakehouse-management/) — execute consultas, navegue no catálogo, faça a gestão de armazéns e monitorize a computação
