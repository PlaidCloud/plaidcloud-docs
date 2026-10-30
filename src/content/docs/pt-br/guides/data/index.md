---
title: Gerenciamento de dados - Tabular
description: Gerencie dados tabulares no PlaidCloud usando tabelas, visões e o mecanismo Lakehouse de alto desempenho para processamento de dados em qualquer escala.
sidebar:
  label: Visão geral
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/index.md
---

A camada de dados do PlaidCloud é construída em torno de **tabelas** (dados estruturados em linhas e colunas) e **visões** (consultas salvas sobre tabelas). Ambas ficam dentro de um projeto e são alimentadas pelo mecanismo Lakehouse, que escala de pequenas tabelas de referência a conjuntos de dados analíticos de bilhões de linhas sem alterações de configuração.

## O que há nesta seção

- [Tabelas e visões](/pt-br/guides/data/tables-views/) — o que cada uma é, quando usar cada uma e como elas interagem
- [Explorador de tabelas](/pt-br/guides/data/table-explorer/) — navegue e inspecione as tabelas do seu projeto
- [Tipo de dados Currency](/pt-br/guides/data/currency-data-type/) — um tipo de coluna exato, de meia largura, para valores monetários, e quando escolhê-lo em vez de Numeric
- [Tipo de dados Vector](/pt-br/guides/data/vector-data-type/) — armazene embeddings pré-calculados em uma tabela de projeto, declare a largura esperada e pesquise as linhas mais próximas
- [Instantâneos de tabela](/pt-br/guides/data/table-snapshots/) — navegue pelo histórico de instantâneos, veja os dados como estavam em um instantâneo anterior e reverta ou restaure uma tabela
- [Publicação de dados](/pt-br/guides/data/publish/) — disponibilize tabelas de projeto para painéis, ferramentas de BI e sistemas downstream, e consulte as orientações de desempenho
- [Selecionando o registro mais recente em uma tabela de histórico grande](/pt-br/guides/data/selecting-latest-record-in-large-history-table/) — um padrão comum com uma solução que leva o desempenho em conta
- [API de geocodificação](/pt-br/guides/data/geocoding-api/) — migre uma integração de geocodificação do Google ou do Mapbox para os endpoints REST de geocodificação do PlaidCloud
- [API de roteamento por tempo de deslocamento](/pt-br/guides/data/drive-time-routing-api/) — prévia opcional: isócronas de tempo de deslocamento de carro e classificação por proximidade em tempo de deslocamento via REST

## De onde vêm os dados

As tabelas costumam ser preenchidas por **fluxos de trabalho** — pipelines automatizados que importam dados, os transformam e gravam os resultados de volta. Consulte [Fluxos de trabalho](/pt-br/guides/workflows/) para saber como criá-los e a [Referência de etapas de fluxo de trabalho](/pt-br/reference/workflow-steps/) para ver todos os tipos de etapa que você pode usar.

Para conectar sistemas externos como fontes de dados, consulte [Conexões (guia)](/pt-br/guides/connections/) e [Conectores (referência)](/pt-br/reference/connectors/).

## Relacionados

- [Conceitos](/pt-br/get-started/concepts/) — como as tabelas se relacionam com fluxos de trabalho, dimensões e o modelo de dados mais amplo
- [Projetos](/pt-br/guides/projects/) — os projetos são donos das tabelas; as tabelas não existem fora de um projeto
- [Painéis](/pt-br/guides/dashboards/) — consomem tabelas publicadas para visualização
