---
title: Notify via Slack
description: Envie notificações do Slack a partir de um passo de fluxo de trabalho do PlaidCloud para alertar canais ou utilizadores sobre eventos, erros e o estado do fluxo de trabalho.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-slack.md
---

Adicionar notificações do Slack a partir de um fluxo de trabalho é um processo em duas partes. As duas partes são:


1. Criar uma ligação externa Webhook do Slack
2. Adicionar passos de notificação do Slack aos seus fluxos de trabalho

## Adicionar o passo de notificação do Slack ao fluxo de trabalho


Adicionar passos de notificação do Slack ao fluxo de trabalho é igual a adicionar outros passos a um fluxo de trabalho. Depois de adicionar o passo, abra a configuração do passo, preencha o formulário e guarde-o. Já pode testar a sua notificação do Slack.



## Anexar um ficheiro

Escolha um documento em **Ficheiro a carregar** para o enviar para o canal, com a mensagem como comentário. Um webhook não consegue transportar um ficheiro, pelo que um anexo passa por um token de bot na ligação do Slack:

- Adicione um **Token de bot** à ligação. É o token `xoxb-` de uma aplicação do Slack com o âmbito `files:write`, e a aplicação tem de ser convidada para o canal.
- Introduza o **ID do canal** no passo, como `C0123ABCD`, e não o nome do canal. O carregamento de ficheiros do Slack só aceita IDs, e o passo falha sem um. Para encontrar um ID, abra os detalhes do canal no Slack e desça até ao fim.
- Se o documento não for encontrado, a mensagem é enviada por webhook sem ele, e o passo avisa com o caminho do documento.

## Formatar a mensagem do Slack


O Slack tem muitas opções de formatação, incluindo adicionar imagens e mencionar utilizadores. Consulte a documentação [Formatação de texto do Slack](https://api.slack.com/reference/surfaces/formatting) para obter detalhes.



## Criar a ligação externa Webhook do Slack


Esta é uma configuração única que permite ao PlaidCloud enviar notificações do Slack em seu nome. O Slack permite criar uma aplicação Webhook (uma forma genérica de enviar uma notificação através da Internet). Depois de criar a aplicação Webhook no Slack, adicione as credenciais fornecidas ao PlaidCloud para permitir a sua utilização.



### Criação da aplicação Webhook do Slack


Estes passos têm de ser realizados por um administrador do Slack. Siga estes passos para criar uma aplicação Webhook do Slack:


1. No Slack, abra o menu de controlo da área de trabalho e selecione `Settings & administration > Manage Apps`
2. Selecione `Custom Integrations` na lista de categorias de aplicações
3. Selecione `Incoming Webhooks` na lista de aplicações
4. Selecione o botão `Add to Slack`
5. No ecrã seguinte, selecione o canal do Slack onde pretende publicar as mensagens e continue. Este é o canal predefinido que será utilizado, mas pode ser substituído em cada notificação, incluindo o envio de mensagens diretas a pessoas específicas.
6. Copie o URL do webhook apresentado. Será utilizado mais tarde, por isso guarde-o num local seguro. Terá um aspeto semelhante a este: `https://hooks.slack.com/services/T04QZ1435/G02TGBFTOP8/K9GZrR2ThdJz1uSiL9YeZxoR`
7. Pode personalizar o aspeto, o nome e o emoji antes de guardar. Estas personalizações são apenas os valores predefinidos e podem ser substituídas em cada passo de notificação de um fluxo de trabalho do PlaidCloud.

### Configuração da ligação externa no PlaidCloud


Estes passos têm de ser realizados por um administrador da área de trabalho do PlaidCloud com permissões para criar Ligações de dados externas. Siga estes passos para criar a ligação:


1. Navegue até `Analyze > Tools > External Data Connections`
2. Em `+ New Connection`, escolha Slack Webhook
3. Preencha o nome, a descrição e cole o URL do webhook fornecido no passo 6 acima. O nome indicado aqui será apresentado como a seleção no passo do fluxo de trabalho, pelo que deve ser o mais descritivo possível. Quem tiver o URL pode publicar no seu canal, pelo que o campo **URL do webhook** o oculta ao colar e aparece em branco quando reabre a ligação; deixe-o em branco para manter o URL guardado.
4. Para enviar anexos, cole também o token de bot da aplicação do Slack no campo **Token de bot (para carregar ficheiros)**. Uma ligação pode conter o URL do webhook, o token de bot, ou ambos. O token de bot é ocultado como o URL do webhook e aparece em branco quando reabre a ligação.
5. Selecione o botão `+ Create`


## Exemplos

Ainda sem exemplos...
