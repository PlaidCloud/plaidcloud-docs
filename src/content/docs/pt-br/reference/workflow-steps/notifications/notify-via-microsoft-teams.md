---
title: Notify via Microsoft Teams
description: Envie notificações do Microsoft Teams a partir de uma etapa de fluxo de trabalho do PlaidCloud para alertar canais ou usuários sobre eventos e o status do fluxo de trabalho.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-microsoft-teams.md
---

Adicionar notificações do Microsoft Teams a partir de um fluxo de trabalho é um processo em duas partes. As duas partes são:


1. Criar uma conexão externa do Microsoft Teams
2. Adicionar etapas de notificação do Microsoft Teams aos seus fluxos de trabalho

## Adicionar a etapa de notificação do Microsoft Teams ao fluxo de trabalho


Adicionar etapas de notificação do Microsoft Teams ao fluxo de trabalho é igual a adicionar outras etapas a um fluxo de trabalho. Ao adicionar a etapa, abra a configuração da etapa, preencha o formulário e salve. Agora você pode testar sua notificação do Microsoft Teams.



## Formatar a mensagem do Microsoft Teams


O Teams tem muitas opções de formatação, incluindo adicionar imagens e mencionar usuários. Consulte a documentação [Formatação de texto de mensagens do Teams](https://support.microsoft.com/en-us/office/use-markdown-formatting-in-teams-4d10bd65-55e2-4b2d-a1f3-2bebdcd2c772) para obter detalhes.



## Criar a conexão externa do Microsoft Teams


Esta é uma configuração única que permite ao PlaidCloud enviar notificações do Microsoft Teams em seu nome. O Microsoft Teams permite criar um aplicativo de webhook (uma forma genérica de enviar uma notificação pela internet). Depois de criar o aplicativo de webhook no Microsoft Teams, adicione as credenciais fornecidas ao PlaidCloud para permitir seu uso.



### Criação do aplicativo de webhook do Microsoft Teams


Estas etapas precisam ser realizadas por um administrador do Microsoft Teams. Siga as etapas descritas aqui para [Criar um webhook de entrada (documentação do Microsoft Teams)](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook#create-incoming-webhook-1).



### Configuração da conexão externa do PlaidCloud


Estas etapas precisam ser realizadas por um administrador do espaço de trabalho do PlaidCloud com permissão para criar Conexões de dados externas. Siga estas etapas para criar a conexão:


1. Acesse `Analyze > Tools > External Data Connections`
2. Em `+ New Connection`, escolha Webhook do Microsoft Teams
3. Preencha o nome, a descrição e cole a URL do webhook gerada durante a criação do webhook acima. O nome informado aqui será exibido como a opção de seleção na etapa do fluxo de trabalho, portanto, se possível, deve ser descritivo. Qualquer pessoa que tenha a URL pode publicar no seu canal, por isso o campo **URL do webhook** a mascara quando você a cola e aparece em branco quando você reabre a conexão; deixe-o em branco para manter a URL salva.
4. Selecione o botão `+ Create`


## Exemplos

Ainda não há exemplos...
