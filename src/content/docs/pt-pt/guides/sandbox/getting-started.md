---
title: Introdução à Sandbox de aplicações personalizadas
description: Comece a criar e a implementar aplicações personalizadas no ambiente Sandbox do PlaidCloud, com os passos de configuração e definição.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/sandbox/getting-started.md
---

## O que é a Sandbox
A Sandbox do PlaidCloud permite implementar as suas próprias aplicações personalizadas com acesso local nativo aos dados e às operações do PlaidCloud.  O ambiente Sandbox fornece um ambiente de computação completo para criar aplicações personalizadas que complementam a sua utilização do PlaidCloud.

Todas as aplicações personalizadas são executadas através de processos de implementação Kubernetes, pelo que é necessário um conhecimento básico dos objetos Kubernetes.  Está disponível um [exemplo Hello World](https://github.com/PlaidCloud/custom-app-template) que mostra como implementar uma aplicação simples.

## Recursos disponíveis
Existe um limite flexível de recursos nas aplicações da Sandbox, com a expectativa de que a utilização de recursos não seja abusiva.  Conseguimos suportar grandes quantidades de computação, se necessário, mas vamos conversar antes de tentar implementar.  Contacte-nos se prevê necessitar de recursos significativos.

As aplicações em execução na Sandbox têm acesso direto ao Lakehouse e a quantas bases de dados Postgres pretender.  As bases de dados Postgres foram concebidas para lidar com dados de tamanho moderado, pelo que são perfeitas para armazenar configurações e outros metadados.  Para o armazenamento principal de dados, utilize o Lakehouse, pois permite armazenar grandes quantidades de dados e manter o desempenho.

Todas as APIs do PlaidCloud estão também disponíveis diretamente a partir da Sandbox sem utilizar um URL público, o que ajuda a obter velocidades de transferência de dados mais rápidas.

## Requisitos das imagens

Qualquer imagem que suporte uma implementação Kubernetes baseada em Docker é adequada para uma aplicação personalizada.  Atualmente, só são suportadas imagens baseadas em *nix.  Se precisar de executar uma imagem baseada em Windows, contacte-nos.

## Integrar com o seu pipeline de CI/CD

A implementação Kubernetes da aplicação Sandbox utiliza processos GitOps.  Isto permite-lhe implementar o seu próprio processo de CI/CD para compilações de imagens e implementações.  O repositório git da sua aplicação personalizada é monitorizado constantemente para detetar alterações, pelo que, à medida que são feitas atualizações, a sua sandbox será atualizada.
