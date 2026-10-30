---
title: Gestão de dados — dados tabulares
description: Faça a gestão de dados tabulares no PlaidCloud com tabelas, vistas e o motor Lakehouse de elevado desempenho, para processamento de dados a qualquer escala.
sidebar:
  label: Descrição geral
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/index.md
---

A camada de dados do PlaidCloud assenta em **tabelas** (dados estruturados em linhas e colunas) e **vistas** (consultas guardadas sobre tabelas). Ambas existem dentro de um projeto e são alimentadas pelo motor Lakehouse, que escala de pequenas tabelas de referência até conjuntos de dados analíticos com milhares de milhões de linhas, sem alterações de configuração.

## O que contém esta secção

- [Tabelas e vistas](/pt-pt/guides/data/tables-views/) — o que é cada uma, quando usar cada uma e como interagem
- [Explorador de tabelas](/pt-pt/guides/data/table-explorer/) — navegue e inspecione as tabelas do seu projeto
- [Tipo de dados Currency](/pt-pt/guides/data/currency-data-type/) — um tipo de coluna exato, de meia largura, para valores monetários, e quando o escolher em vez de Numeric
- [Tipo de dados Vector](/pt-pt/guides/data/vector-data-type/) — guarde embeddings pré-calculados numa tabela de projeto, declare a largura esperada e pesquise as linhas mais próximas
- [Instantâneos de tabelas](/pt-pt/guides/data/table-snapshots/) — consulte o histórico de instantâneos, veja os dados tal como estavam num instantâneo anterior e reverta ou restaure uma tabela
- [Publicar dados](/pt-pt/guides/data/publish/) — disponibilize tabelas de projeto a painéis de controlo, ferramentas de BI e sistemas a jusante, e consulte as recomendações de desempenho
- [Selecionar o registo mais recente numa tabela de histórico grande](/pt-pt/guides/data/selecting-latest-record-in-large-history-table/) — um padrão comum com uma solução orientada para o desempenho
- [API de geocodificação](/pt-pt/guides/data/geocoding-api/) — migre uma integração de geocodificação da Google ou do Mapbox para os endpoints REST de geocodificação do PlaidCloud
- [API de encaminhamento por tempo de condução](/pt-pt/guides/data/drive-time-routing-api/) — pré-visualização opcional: isócronas de tempo de condução e classificação por proximidade em tempo de condução através de REST

## De onde vêm os dados

As tabelas são normalmente preenchidas por **fluxos de trabalho** — pipelines automatizados que importam dados, os transformam e escrevem os resultados de volta. Consulte [Fluxos de trabalho](/pt-pt/guides/workflows/) para saber como os criar e a [referência de passos de fluxo de trabalho](/pt-pt/reference/workflow-steps/) para ver todos os tipos de passo que pode utilizar.

Para ligar sistemas externos como origens de dados, consulte [Ligações (guia)](/pt-pt/guides/connections/) e [Conectores (referência)](/pt-pt/reference/connectors/).

## Relacionado

- [Conceitos](/pt-pt/get-started/concepts/) — como as tabelas se relacionam com fluxos de trabalho, dimensões e o modelo de dados em geral
- [Projetos](/pt-pt/guides/projects/) — os projetos são proprietários das tabelas; as tabelas não existem fora de um projeto
- [Painéis de controlo](/pt-pt/guides/dashboards/) — consomem tabelas publicadas para visualização
