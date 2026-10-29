---
title: Notify via Microsoft Teams
description: Envie notificações do Microsoft Teams a partir de um passo de fluxo de trabalho do PlaidCloud para alertar canais ou utilizadores sobre eventos e o estado do fluxo de trabalho.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-microsoft-teams.md
---

Adicionar notificações do Microsoft Teams a partir de um fluxo de trabalho é um processo em duas partes. As duas partes são:


1. Criar uma ligação externa ao Microsoft Teams
2. Adicionar passos de notificação do Microsoft Teams aos seus fluxos de trabalho

## Adicionar o passo de notificação do Microsoft Teams ao fluxo de trabalho


Adicionar passos de notificação do Microsoft Teams ao fluxo de trabalho é igual a adicionar outros passos a um fluxo de trabalho. Depois de adicionar o passo, abra a configuração do passo, preencha o formulário e guarde-o. Já pode testar a sua notificação do Microsoft Teams.



## Formatar a mensagem do Microsoft Teams


O Teams tem muitas opções de formatação, incluindo adicionar imagens e mencionar utilizadores. Consulte a documentação [Formatação de texto de mensagens do Teams](https://support.microsoft.com/en-us/office/use-markdown-formatting-in-teams-4d10bd65-55e2-4b2d-a1f3-2bebdcd2c772) para obter detalhes.



## Criar a ligação externa ao Microsoft Teams


Esta é uma configuração única que permite ao PlaidCloud enviar notificações do Microsoft Teams em seu nome. O Microsoft Teams permite criar uma aplicação Webhook (uma forma genérica de enviar uma notificação através da Internet). Depois de criar a aplicação Webhook no Microsoft Teams, adicione as credenciais fornecidas ao PlaidCloud para permitir a sua utilização.



### Criação da aplicação Webhook do Microsoft Teams


Estes passos têm de ser realizados por um administrador do Microsoft Teams. Siga os passos descritos aqui para [Criar um webhook de entrada (documentação do Microsoft Teams)](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook#create-incoming-webhook-1).



### Configuração da ligação externa no PlaidCloud


Estes passos têm de ser realizados por um administrador da área de trabalho do PlaidCloud com permissões para criar Ligações de dados externas. Siga estes passos para criar a ligação:


1. Navegue até `Analyze > Tools > External Data Connections`
2. Em `+ New Connection`, escolha Microsoft Teams Webhook
3. Preencha o nome, a descrição e cole o URL do webhook gerado durante a criação do webhook acima. O nome indicado aqui será apresentado como a seleção no passo do fluxo de trabalho, pelo que deve ser o mais descritivo possível. Quem tiver o URL pode publicar no seu canal, pelo que o campo **URL do webhook** o oculta ao colar e aparece em branco quando reabre a ligação; deixe-o em branco para manter o URL guardado.
4. Selecione o botão `+ Create`


## Exemplos

Ainda sem exemplos...
