---
title: Primeiros passos com o sandbox de aplicativos personalizados
description: Comece a criar e implantar aplicativos personalizados no ambiente Sandbox do PlaidCloud, com as etapas de configuração e instalação.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/sandbox/getting-started.md
---

## O que é o Sandbox
O Sandbox do PlaidCloud permite implantar seus próprios aplicativos personalizados com acesso local nativo a dados e operações do PlaidCloud.  O ambiente Sandbox oferece um ambiente de computação completo para criar aplicativos personalizados que ampliam o seu uso do PlaidCloud.

Todos os aplicativos personalizados são executados por meio de processos de implantação do Kubernetes, portanto é necessário um conhecimento básico dos objetos do Kubernetes.  Há um [exemplo Hello World](https://github.com/PlaidCloud/custom-app-template) que mostra como implantar um aplicativo simples.

## Recursos disponíveis
Os aplicativos do Sandbox têm um limite flexível de recursos, com a expectativa de que o uso não seja abusivo.  Podemos oferecer grandes quantidades de computação, se necessário, mas converse conosco antes de tentar implantar.  Entre em contato se você espera precisar de recursos significativos.

Os aplicativos executados no sandbox têm acesso direto ao Lakehouse e a quantos bancos de dados Postgres você quiser.  Os bancos de dados Postgres foram projetados para dados de tamanho moderado, por isso são ideais para armazenar configurações e outros metadados.  Para o armazenamento principal de dados, use o Lakehouse, pois ele permite armazenar grandes volumes de dados sem perder desempenho.

Todas as APIs do PlaidCloud também ficam disponíveis diretamente no Sandbox, sem usar uma URL pública, o que ajuda na velocidade de transferência de dados.

## Requisitos de imagem

Qualquer imagem que ofereça suporte a uma implantação do Kubernetes baseada em Docker é adequada para um aplicativo personalizado.  Atualmente, só há suporte para imagens baseadas em *nix.  Se você precisa executar uma imagem baseada em Windows, entre em contato conosco.

## Integre com seu pipeline de CI/CD

A implantação do aplicativo Sandbox no Kubernetes utiliza processos de GitOps.  Isso permite implementar seu próprio processo de CI/CD para compilações e implantações de imagens.  O repositório git do seu aplicativo personalizado é monitorado constantemente em busca de alterações, de modo que, conforme as atualizações são feitas, seu sandbox é atualizado.
