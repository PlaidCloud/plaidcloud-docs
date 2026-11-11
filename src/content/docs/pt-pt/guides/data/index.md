---
title: Gestão de dados — tabulares
description: Faça a gestão de dados tabulares no PlaidCloud com tabelas, vistas e o motor Lakehouse de alto desempenho, para processar dados a qualquer escala.
sidebar:
  label: Descrição geral
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/data/index.md
---

A camada de dados do PlaidCloud assenta em **tabelas** (dados estruturados em linhas e colunas) e **vistas** (consultas guardadas sobre tabelas). Ambas residem dentro de um projeto e são suportadas pelo motor Lakehouse, que escala de pequenas tabelas de referência até conjuntos de dados analíticos com milhares de milhões de linhas sem alterações de configuração.

## O que contém esta secção

- [Tabelas e vistas](/pt-pt/guides/data/tables-views/) — o que é cada uma, quando utilizar qual e como interagem
- [Explorador de tabelas](/pt-pt/guides/data/table-explorer/) — procure e inspecione as tabelas do seu projeto
- [Tipo de dados Currency](/pt-pt/guides/data/currency-data-type/) — um tipo de coluna exato, com metade da largura, para valores monetários, e quando o escolher em vez de Numeric
- [Tipo de dados Vector](/pt-pt/guides/data/vector-data-type/) — armazene embeddings pré-calculados numa tabela do projeto, declare a largura esperada e pesquise as linhas mais próximas
- [Instantâneos de tabelas](/pt-pt/guides/data/table-snapshots/) — percorra o histórico de instantâneos, veja os dados tal como estavam num instantâneo anterior e reverta ou restaure uma tabela
- [A janela Lakehouse](/pt-pt/guides/data/lakehouse-window/) — acompanhe e analise o perfil de consultas, percorra catálogos e tabelas com os respetivos instantâneos e copie uma consulta de viagem no tempo
- [Publicar dados](/pt-pt/guides/data/publish/) — disponibilize tabelas do projeto a painéis de controlo, ferramentas de BI e sistemas a jusante, e consulte as respetivas recomendações de desempenho
- [Selecionar o registo mais recente numa grande tabela de histórico](/pt-pt/guides/data/selecting-latest-record-in-large-history-table/) — um padrão comum com uma solução que tem em conta o desempenho
- [API de geocodificação](/pt-pt/guides/data/geocoding-api/) — migre uma integração de geocodificação da Google ou da Mapbox para os endpoints REST de geocodificação do PlaidCloud
- [API de rotas por tempo de condução](/pt-pt/guides/data/drive-time-routing-api/) — pré-visualização opcional: isócronas de tempo de condução e classificação por proximidade em tempo de condução através de REST

## De onde vêm os dados

As tabelas são normalmente preenchidas por **fluxos de trabalho** — pipelines automatizados que importam dados, os transformam e escrevem os resultados. Consulte [Fluxos de trabalho](/pt-pt/guides/workflows/) para saber como criá-los e a [Referência de passos de fluxos de trabalho](/pt-pt/reference/workflow-steps/) para conhecer todos os tipos de passo que pode utilizar.

Para ligar sistemas externos como origens de dados, consulte [Ligações (guia)](/pt-pt/guides/connections/) e [Conectores (referência)](/pt-pt/reference/connectors/).

## Relacionado

- [Conceitos](/pt-pt/get-started/concepts/) — como as tabelas se relacionam com os fluxos de trabalho, as dimensões e o modelo de dados mais amplo
- [Projetos](/pt-pt/guides/projects/) — os projetos são proprietários das tabelas; as tabelas não existem fora de um projeto
- [Painéis de controlo](/pt-pt/guides/dashboards/) — utilizam tabelas publicadas para visualização
